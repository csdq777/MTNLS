export CUDA_VISIBLE_DEVICES=0

cd ../src

# please modify --model_path before running the following commands

# x to chinese
python3 main.py \
--src_lang mn \
--tgt_lang zh \
--dict_path ../data/mn_zh_dict.jsonl \
--corpus_path ../data/zh_mn_train.json \
--test_data_path ../data/zh_mn_test.json \
--model_name Llama-3.1-8B-Instruct \
--model_path /root/autodl-tmp/MTNLS/models/Llama-3.1-8B-Instruct \
--prompt_type za2zh \
--num_parallel_sent 3 \
--no_vllm \
--output_path ../output/Llama-3.1-8B-Instruct_mn2zh.jsonl 


# chinese to x
python3 main.py \
--src_lang zh \
--tgt_lang mn \
--dict_path ../data/zh_mn_dict.jsonl \
--corpus_path ../data/zh_mn_train.json \
--test_data_path ../data/zh_mn_test.json \
--model_name Llama-3.1-8B-Instruct \
--model_path /root/autodl-tmp/MTNLS/models/Llama-3.1-8B-Instruct \
--prompt_type zh2za \
--num_parallel_sent 3 \
--no_vllm \
--output_path ../output/Llama-3.1-8B-Instruct_zh2mn.jsonl 

