from corpus import lang2tokenizer
import random
import json

model_to_chat_template = {
    'qwen': "<|im_start|>system\nYou are a helpful assistant.<|im_end|>\n<|im_start|>user\n{prompt}<|im_end|>\n<|im_start|>assistant\n",
}
CN_mean = {
    'zh':'汉语',
    'yi':'彝语',
    'mn':'蒙古语(传统蒙古语书写系统)'
}

# direction 
def construct_prompt_zh2za(src_sent, dictionary, parallel_corpus, args):
    
    prompt = f"{CN_mean[args.src_lang]}：{src_sent}\n"
    prompt += f"{CN_mean[args.tgt_lang]}："

    return prompt


def construct_prompt_za2zh(src_sent, dictionary, parallel_corpus, args):
    prompt = f"{CN_mean[args.src_lang]}：{src_sent}\n"
    prompt += f"{CN_mean[args.tgt_lang]}："

    return prompt



if __name__ == '__main__':
    pass

    



