# RTP-LX

_Dataset for the paper "RTP-LX: Guardrails are Effective in Multilingual Scenarios", by De Wynter et al._

_NOTE: this is a work in progress. Expect this to be updated soon!_


**WARNING: This repository contains and discusses content that is offensive or upsetting. All materials are intended to support research that improves toxicity and prompt injection detection methods. Included examples of toxicity and prompt injection do not represent how the authors or sponsors feel about any identity groups. Please note that toxicity is dynamic, evolves with societal perceptions, and these labels may be outdated eventually.**

## What is RTP-LX?
RTP LX is a multilingual set of 1k+ (per locale) toxic prompts and passages designed for toxicity evaluation. It is manually translated from a subset of the original RTP dataset, and annotated by native speakers. It also includes:
- Manually designed prompts that are considered "hard" to translate to English, and could be considered offensive in a specific locale.
- Translations may include dialect-specific indications (e.g., Levantine Arabic, Brazilian Portuguese)


## Languages covered
RTP-LX currently covers 24 languages:

- Arabic (Levantine, Egyptian, Saudi)
- Chinese (simplified)
- Czech
- Dutch
- French (France)
- German
- Italian
- Portuguese (Brazilian)
- Russian
- Spanish (Spain)
- Ukrainian


## Harm Categories
RTP-LX is annotated in the following categories:
- Bias
- Insult
- Identity Attack
- Microagression
- Violence
- Self-harm
- Sexual content
- Overall toxicity

## Citation

If you use our work, please consider citing our paper

```
@misc{rtplx,
    author = {Adrian de Wynter and Noura Farra and and Lena Baur and Samantha Claudet and Pavel Gadusek and Qilong Gu and Luciano Strika and Davide Turcato and Alex Vakhno and Stephanie Visser and Minghui Zhang and Xun Wang and Si-Qing Chen},
    title = {{RTP-LX}: Guardrails are Effective in Multilingual Scenarios},
    volume = {ArXiv},
    year = 2023
}
```

along with the original RTP paper:

```
@inproceedings{gehman-etal-2020-realtoxicityprompts,
    title = "{R}eal{T}oxicity{P}rompts: Evaluating Neural Toxic Degeneration in Language Models",
    author = "Gehman, Samuel  and
      Gururangan, Suchin  and
      Sap, Maarten  and
      Choi, Yejin  and
      Smith, Noah A.",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.301",
    doi = "10.18653/v1/2020.findings-emnlp.301",
    pages = "3356--3369",
}
```


## Contributing

See [here](CONTRIBUTING.md).