# RTP-LX

_Dataset for the paper [RTP-LX: Can LLMs Evaluate Toxicity in Multilingual Scenarios?](https://arxiv.org/abs/2404.14397), by De Wynter et al._

_NOTE: this is a work in progress. Expect this to be updated soon!_

**WARNING: This repository contains and discusses content that is offensive or upsetting. All materials are intended to support research that improves toxicity detection methods. Included examples of toxicity do not represent how the authors or sponsors feel about any identity groups. This corpus was made by a multi-national, multi-cultural team of various faiths, beliefs, and origins. Please note that toxicity is dynamic, evolves with societal perceptions, and these labels may change.**


## What is RTP-LX?
RTP LX is a multilingual set of 1k+ (per locale) toxic prompts and passages designed for toxicity evaluation. It is manually translated from a subset of the original RTP dataset, and annotated by native speakers. It also includes:
- Coverage in 27 languages (28 because we split ZH-Hans and ZH-Hant)
- Manually designed prompts that are considered "hard" to translate to English, and could be considered offensive in the language's geolocale.
- Translations may include dialect-specific indications (e.g., Levantine Arabic, Brazilian Portuguese)


## Languages covered
RTP-LX currently covers 27 languages:

- Arabic (Egyptian, Levantine, Saudi)
- BCMS
- Chinese (simplified, traditional)
- Czech
- Danish
- Dutch
- English
- Finnish
- French (France)
- German
- Hebrew
- Hindi
- Hungarian
- Indonesian
- Italian
- Japanese
- Korean
- Norwegian (Bokmål)
- Polish
- Portuguese (Brazilian, Portuguese)
- Russian (Russia, Ukraine)
- Spanish (Spain)
- Swahili
- Swedish
- Thai
- Turkish
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

## Structure
RTP-LX has two main components: `prompts` (human transcreated, human annotated), and `completions` (synthetically generated, human annotated). `Prompts` are meant to measure the effectiveness of your guardrails in multilingual scenarios, as well as automated annotation capabilities. 
`Completions`, on the other hand, are much, much more toxic and are designed for ablation analysis of harm categories.

## Uncompressing

To avoid crawlers, we have zipped and password-protected the entries. Please use the name of the repo all in lowercase plus "-entries" and `-16/4/24` as the password. So if the repo is "ASDF-BLAH", you want `asdf-blah-entries-16/4/24`.

## Updates:
- (Apr '22): Paper released!
- (Mar '24): V1.0 released! Passages annotated. This is the first full release of RTP-LX. We do have updates coming, so stay tuned.
- (Jan '24): V0.3 released! Added SW/BCMS. Compressed to file. Passages to come soon.
- (Dec '23): V0.2 released! Added 19 more languages, and included PT (pt) prompts. Note that BCMS/Swahili are projected for a later date.
- (Sep '23): V0.1 released! Prompts for ES, FR, DE, IT, JA, PT (br), ZH (simplified), AR and CS.

## Citation

If you use our work, please consider citing our paper (_coming soon! Just cite the repo for now_)

```
@misc{rtplx,
    author = {Adrian de Wynter and Ishaan Watts and Nektar Ege Alt{\i}ntoprak and Tua Wongsangaroonsri and Minghui Zhang and Noura Farra and Lena Baur and Samantha Claudet and Pavel Gajdusek and Can G\"oren and Qilong Gu and Anna Kaminska and Tomasz Kaminski and Ruby Kuo and Akiko Kyuba and Jongho Lee and Kartik Mathur and Petter Merok and Ivana Milovanovi\'c and Nani Paananen and Vesa-Matti Paananen and Anna Pavlenko and Bruno Pereira Vidal and Luciano Strika and Yueh Tsao and Davide Turcato and Oleksandr Vakhno and Judit Velcsov and Anna Vickers and St\'ephanie Visser and Herdyan Widarmanto and Andrey Zaikin and Si-Qing Chen},
    title = {{RTP-LX}: Can {LLMs} Evaluate Toxicity in Multilingual Scenarios?},
    volume = {ArXiv},
    url = {https://arxiv.org/abs/2404.14397},
    volume={abs/2404.14397},
    doi={10.48550/arXiv.2404.14397}
    year = 2024
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

Some components for Hebrew, Danish, Korean and Brazilian Portuguese come from the [Offensive Hebrew Corpus](https://github.com/SinaLab/OffensiveHebrew/tree/main), [DKHate](https://aclanthology.org/2020.lrec-1.430/), [BEEP!](https://github.com/kocohub/korean-hate-speech/tree/master) and [ToLD-BR](https://github.com/JAugusto97/ToLD-Br) corpora, respectively. Please consider citing their work as well:

```
@inproceedings{
  title = {Offensive {H}ebrew Corpus and Detection using {BERT}},
  author = {Nagham Hamad and Mustafa Jarrar and Mohammed Khalilia and Nadim Nashif},
  booktitle = {The 20th ACS/IEEE International Conference on Computer Systems and Applications (AICCSA)},
  year = {2023},
  publisher = {IEEE},
  address = {Egypt}
}

@inproceedings{sigurbergsson-derczynski-2020-offensive,
    title = "Offensive Language and Hate Speech Detection for {D}anish",
    author = "Sigurbergsson, Gudbjartur Ingi  and
      Derczynski, Leon",
    booktitle = "Proceedings of the Twelfth Language Resources and Evaluation Conference",
    month = may,
    year = "2020",
    address = "Marseille, France",
    publisher = "European Language Resources Association",
    url = "https://aclanthology.org/2020.lrec-1.430",
    pages = "3498--3508",
    language = "English",
    ISBN = "979-10-95546-34-4",
}

@inproceedings{moon-etal-2020-beep,
    title = "{BEEP}! {K}orean Corpus of Online News Comments for Toxic Speech Detection",
    author = "Moon, Jihyung  and
      Cho, Won Ik  and
      Lee, Junbum",
    booktitle = "Proceedings of the Eighth International Workshop on Natural Language Processing for Social Media",
    month = jul,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.socialnlp-1.4",
    pages = "25--31",
}

@inproceedings{ToLDBR,
  author = {Jo\~{a}o A. Leite and Diego F. Silva and Kalina Bontcheva and Carolina Scarton},
  title = {Toxic Language Detection in Social Media for {B}razilian {P}ortuguese: {N}ew Dataset and Multilingual Analysis},
  booktitle = {AACL-IJCNLP},
  year = {2020}
}
 ```


## Contributing

See [here](CONTRIBUTING.md).
