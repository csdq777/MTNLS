import json
import numpy as np
import argparse
import re
from tokenizer import YiTokenizer
from sacrebleu.metrics import BLEU, CHRF


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output_path', type=str, default='pred.jsonl')
    parser.add_argument('--lang', type=str, default='zh')
    parser.add_argument('--leveled', action='store_true')
    args = parser.parse_args()

    
    if args.lang == 'zh':
        chrfpp = CHRF(word_order=2, lowercase=True)
        chrf = CHRF(word_order=0, lowercase=True)
        scarebleu = BLEU(lowercase=True, tokenize='zh')  
    elif args.lang == 'yi':
        chrfpp = CHRF(word_order=2, lowercase=True)  
        chrf = CHRF(word_order=0, lowercase=True)    
        scarebleu = BLEU(lowercase=True, tokenize='none')  
    elif args.lang == 'mn':
        chrfpp = CHRF(word_order=2, lowercase=True)
        chrf = CHRF(word_order=0, lowercase=True)
        scarebleu = BLEU(lowercase=True)  
    
    # Load data from the output file
    output = []
    with open(args.output_path, "r") as f:
        for line in f:
            line = json.loads(line)
            output.append(line)

    metrics = {}
    refs = []
    preds = []
    
    yi_tokenizer = YiTokenizer()  # Initialize Yi tokenizer

    # Process the predictions and references for different languages
    for item in output:
        
        # For Yi language, tokenize manually
        if args.lang == 'yi':
            item['gold'] = " ".join(yi_tokenizer.tokenize(item['gold']))  # Tokenize gold standard text
            item['pred'] = " ".join(yi_tokenizer.tokenize(item['pred']))  # Tokenize predicted text
        
        refs.append(item['gold'])
        preds.append(item['pred'])

    refs = [refs]
    
    # Calculate metrics
    metrics['sacrebleu'] = scarebleu.corpus_score(preds, refs).score
    metrics['chrf++'] = chrfpp.corpus_score(preds, refs).score
    metrics['chrf'] = chrf.corpus_score(preds, refs).score
    
    # Round the metrics to 4 decimal places
    for key in ['sacrebleu', 'chrf++', 'chrf']:
        metrics[key] = np.around(metrics[key], decimals=4)
    
    # Print overall metrics
    print("Overall metrics:")
    print(metrics)

    # If `leveled` flag is set, calculate metrics by difficulty level
    if args.leveled:
        metrics_by_level = {}
        for level in ['easy', 'medium', 'hard']:
            refs = []
            preds = []
            for i, item in enumerate(output):
                if item['source'] == level:
                    # For Yi language, tokenize manually
                    if args.lang == 'yi':
                        item['gold'] = " ".join(yi_tokenizer.tokenize(item['gold']))
                        item['pred'] = " ".join(yi_tokenizer.tokenize(item['pred']))
                    refs.append(item['gold'])
                    preds.append(item['pred'])
            refs = [refs]
            metrics_by_level[level] = {}
            metrics_by_level[level]['sacrebleu'] = scarebleu.corpus_score(preds, refs).score
            metrics_by_level[level]['chrf++'] = chrfpp.corpus_score(preds, refs).score
            metrics_by_level[level]['chrf'] = chrf.corpus_score(preds, refs).score
            
            # Round the metrics for each level
            for key in ['sacrebleu', 'chrf++', 'chrf']:
                metrics_by_level[level][key] = np.around(metrics_by_level[level][key], decimals=4)
            
            # Print metrics by difficulty level
            print(f"Metrics for {level} level:")
            print(metrics_by_level[level])
