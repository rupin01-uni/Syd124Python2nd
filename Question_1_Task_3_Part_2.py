# https://github.com/rupin01-uni/Syd124Python2nd

import os
import pandas as pd
from collections import Counter
from transformers import AutoTokenizer
import time
from concurrent.futures import ThreadPoolExecutor
import itertools

def tokenize_chunk(chunk, tokenizer):
    encoding = tokenizer.batch_encode_plus([chunk], return_tensors="pt", max_length=512, truncation=True)
    tokens = tokenizer.convert_ids_to_tokens(encoding['input_ids'][0])
    return tokens

def count_unique_tokens(text_file_path, top_n=30, max_chunks=None):
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
    start_time = time.time()
    unique_token_counts = Counter()
    chunk_size = 50000

    with open(text_file_path, 'r', encoding='utf-8') as file:
        chunks = iter(lambda: file.read(chunk_size), '')
        if max_chunks:
            chunks = itertools.islice(chunks, max_chunks)

        with ThreadPoolExecutor() as executor:
            for i, tokens in enumerate(executor.map(lambda chunk: tokenize_chunk(chunk, tokenizer), chunks)):
                unique_token_counts.update(set(tokens))

    top_n_tokens = unique_token_counts.most_common(top_n)
    top_n_df = pd.DataFrame(top_n_tokens, columns=['Token', 'Count'])
    csv_file_path = os.path.join(os.getcwd(), 'top_30_tokens.csv')
    top_n_df.to_csv(csv_file_path, index=False)

output_txt_file_path = os.path.join(os.getcwd(), "output_text_file.txt")
count_unique_tokens(output_txt_file_path, max_chunks=10)
