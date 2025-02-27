cd ../src

# x to chinese
python eval.py \
        --output_path ../output/Llama-3.1-8B-Instruct_mn2zh.jsonl   \
        --lang zh \
        --leveled

# chinese to x
python eval.py \
        --output_path ../output/Llama-3.1-8B-Instruct_zh2mn.jsonl    \
        --lang mn \
        --leveled
