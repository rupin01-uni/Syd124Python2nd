import pandas as pd
import os
import zipfile
import shutil

zipped_folder_relative_path = "Assignment 2.zip"
zipped_folder_path = os.path.join(os.getcwd(), zipped_folder_relative_path)

extracted_folder_path = os.path.join(os.getcwd(), "Assignment 2_Extracted")
os.makedirs(extracted_folder_path, exist_ok=True)

with zipfile.ZipFile(zipped_folder_path, 'r') as zip_ref:
    zip_ref.extractall(extracted_folder_path)

all_texts = []

for file_name in os.listdir(extracted_folder_path):
    if file_name.endswith('.csv'):
        file_path = os.path.join(extracted_folder_path, file_name)
        df = pd.read_csv(file_path)

        texts_per_row = []
        for _, row in df.iterrows():
            largest_text_in_row = max(row.astype(str), key=len)
            texts_per_row.append(largest_text_in_row)

        all_texts.extend(texts_per_row)

output_txt_file = os.path.join(os.getcwd(), "output_text_file.txt")
with open(output_txt_file, 'w', encoding='utf-8') as txt_file:
    txt_file.write('\n'.join(all_texts))
