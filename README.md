#  Can LLMs Translate Unseen Languages in Non-Latin Scripts?

![image](https://github.com/user-attachments/assets/50a5ae28-f57b-470c-97f1-14e23d264f86)


### Dataset

We propose the MTNLS Benchmark, a suite for NLP research, including two non-Latin script languages unseen by LLMs: Mongolian (traditional script) and Yi. This suite mainly consists of bilingual dictionaries, parallel corpora, and word segmentation tools for each language, designed to support machine translation tasks.

- `data\yi_token_dict.txt`: Yi words for segmentation.  
- `data\yi_zh_dict.jsonl`: Yi-to-Chinese dictionary.  
- `data\zh_yi_dict.jsonl`: Chinese-to-Yi dictionary.  
- `data\zh_mn_dict.jsonl`: Chinese-to-Mongolian dictionary.  
- `data\mn_zh_dict.jsonl`: Mongolian-to-Chinese dictionary.  
- `data\zh_mn_train.json`: Chinese-Mongolian training data.  
- `data\zh_mn_test.json`: Chinese-Mongolian test data.  
- `data\zh_yi_train.json`: Chinese-Yi training data.  
- `data\zh_yi_test.json`: Chinese-Yi test data.

To prevent test set contamination, we encrypted the source files of the MTNLS Benchmark in `data.zip`. The password is `mtnlsdata`.

### Code

Install the dependencies:

```bash
pip install -r requirements.txt
```

The following prompt files represent different prompting strategies we provide to LLMs.

- `src\prompt.py`: DIPMT++ _w/o fuzzy_ .  
- `src\prompt_DIPMT++.py`: DIPMT++.  
- `src\prompt_DIPMT.py`: DIPMT.  
- `src\prompt_ICL.py`: ICL (In-Context Learning).  
- `src\prompt_direc.py`: Represents code for directly prompting LLMs.

You can use `scripts\run.sh` to run the LLM and then use `scripts\eval.sh` to evaluate machine translation  performance.

### License

The code is licensed under MIT, and the data is licensed under CC BY-NC 4.0.



