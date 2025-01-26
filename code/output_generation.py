import os
import torch
import json
from tqdm import tqdm
import gc
import openai
import backoff
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from constants import SYSTEM_MESSAGE, INSTRUCTIONS, EXAMPLES, MODELS, MODEL_MAP
import warnings
from dotenv import load_dotenv
load_dotenv()
import sys
warnings.simplefilter(action='ignore')



def llama2_mistral_prompt(prompt):
    input_prompt = f"<s>[INST] <<SYS>>\n{SYSTEM_MESSAGE}\n<</SYS>>\n{INSTRUCTIONS}\n[/INST]\n{EXAMPLES} {prompt}\n\nResponse:\n"
    return input_prompt

def llama3_prompt(prompt):
    input_prompt = f'<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\n{SYSTEM_MESSAGE}\n\n{INSTRUCTIONS}<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n{EXAMPLES} {prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>Response:\n'
    return input_prompt

def gemma_prompt(prompt):
    input_prompt = f"<bos><start_of_turn>user\n{SYSTEM_MESSAGE}\n\n{INSTRUCTIONS}<end_of_turn>\n<start_of_turn>model\n\n{EXAMPLES} {prompt}\n\nResponse:\n"
    return input_prompt

def gpt_prompt(prompt):
    input_prompt = [
        {"role": "system", "content": f"{SYSTEM_MESSAGE}\n\n{INSTRUCTIONS}\n\n{EXAMPLES}"},
        {"role": "user", "content": prompt}
    ]
    return input_prompt

@backoff.on_exception(
    backoff.expo,
    Exception,
    max_time=600,
    max_tries=3,
)
def get_gpt4_response(model, model_name, input_prompt):
    response = model.chat.completions.create(
        model=model_name,
        messages=input_prompt,
        max_tokens=200,
        
    ).choices[0].message.content
    return response
    

def run_inference(model_name, input_dir, output_dir, eval_type="Prompt", device_number=0):

    device = torch.device(f'cuda:{device_number}' if torch.cuda.is_available() else 'cpu')
    print("Using device:", device)

    folder_name = MODEL_MAP[model_name]
    if "gpt" in model_name:
        model = openai.AzureOpenAI(
            azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
            api_key=os.getenv("AZURE_OPENAI_KEY"),  
            api_version="2023-05-15"
            )
    else:
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16) #, device_map = 'auto'
        pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, device=device)

    os.makedirs(os.path.join(output_dir, folder_name), exist_ok=True)

    for file in os.listdir(input_dir)[7*int(device_number):7*(int(device_number)+1)]:
        language = file.split("_")[2][:-5]
        dataset = [json.loads(line) for line in open(os.path.join(input_dir, file), "r", encoding="utf-8").readlines()]
        try:
            start_idx = len([json.loads(line) for line in open(os.path.join(output_dir, folder_name, f"results_{language}.jsonl"), "r", encoding="utf-8").readlines()])
        except Exception as e:
            start_idx = 0

        print("Starting from index:", start_idx)
        
        for idx, obj in enumerate(tqdm(dataset, desc=f"Running inference for {language}")):
            if idx < start_idx:
                continue
            
            if "gemma" in model_name:
                input_prompt = gemma_prompt(obj[eval_type])
            elif "gpt" in model_name:
                input_prompt = gpt_prompt(obj[eval_type])
            elif "Llama-3" in model_name:
                input_prompt = llama3_prompt(obj[eval_type])
            else:
                input_prompt = llama2_mistral_prompt(obj[eval_type])
                
            if "gpt" in model_name:
                try:
                    response = get_gpt4_response(model, model_name, input_prompt)
                except Exception as e:
                    print("ERROR", e)
                    response = "ERROR"  
            else:
                response = pipe(input_prompt, max_new_tokens=200)[0]['generated_text'].removeprefix(input_prompt)
            new_point = {
                eval_type: obj[eval_type],
                "InputPrompt" : input_prompt,
                "ResponseRaw": response,
                "Locale": language,
                "Index": obj["Index"],
                "OriginalEntry": obj
            }

            with open(os.path.join(output_dir, folder_name, f"results_{language}.jsonl"), "a", encoding="utf-8") as file:
                file.write(json.dumps(new_point, ensure_ascii=False) + "\n")   

def main(models, eval_type, device_number):
    for model in models:
        print(f"Running inference for: {model}")
        run_inference(model, input_dir="datasets/RTP_LX", output_dir=f"llm_eval/{eval_type.lower()}/raw_outputs_new/", eval_type=eval_type, device_number=device_number)
        gc.collect()
        torch.cuda.empty_cache()

if __name__ == "__main__":
    args = sys.argv
    eval_type = sys.argv[1]
    device_number = sys.argv[2]
    models = sys.argv[3:]
    if not models:
        models = MODELS
    print(models)
    main(models, eval_type, device_number)



