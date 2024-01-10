

from collections import Counter
import csv


word_counts = Counter()

with open('combined_text.txt', 'r', encoding='utf-8') as file:
    for line in file:
        words = line.split()
        word_counts.update(words)

top_30_words = word_counts.most_common(30)

with open('top_30_words.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Word', 'Count'])
    csv_writer.writerows(top_30_words)

tokens = biobert_tokenizer.tokenize(biobert_tokenizer.decode(biobert_tokenizer.encode(text)))
token_counts = Counter(tokens)

top_30_tokens = token_counts.most_common(30)


    