# https://github.com/rupin01-uni/Syd124Python2nd


import os
import pandas as pd
from collections import Counter
import time

output_txt_file = os.path.join(os.getcwd(), "output_text_file.txt")

start_time = time.time()

chunk_size = 100000
word_counts = Counter()

with open(output_txt_file, 'r', encoding='utf-8') as file:
    for chunk in iter(lambda: file.read(chunk_size), ''):
        words = chunk.split()
        word_counts.update(words)

top_30_words = word_counts.most_common(30)
top_30_df = pd.DataFrame(top_30_words, columns=['Word', 'Count'])
csv_file_path = os.path.join(os.getcwd(), 'top_30_words.csv')
top_30_df.to_csv(csv_file_path, index=False)
