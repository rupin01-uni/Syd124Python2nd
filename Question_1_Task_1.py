import pandas as pd
import zipfile
import os


zip_folder_path = 'D:\Software_now_project\Assignment 2.zip'
output_folder = 'D:\Software_now_project'
with zipfile.ZipFile(zip_folder_path, 'r') as zip_ref:
    zip_ref.extractall(output_folder)


output_text_file = 'output_text.txt'
text_data = []


with open(output_text_file, 'w', encoding='utf-8') as txt_file:
    for root, dirs, files in os.walk(output_folder):
        for file in files:
            if file.endswith(".csv"):
                csv_path = os.path.join(root, file)
                for chunk in pd.read_csv(csv_path, chunksize=1000):  
                    if "SHORT_TEXT" in chunk.columns:
                        for text in chunk["SHORT_TEXT"].astype(str):
                            txt_file.write(text + '\n')
                    elif "TEXT" in chunk.columns:
                        for text in chunk["TEXT"].astype(str):
                            txt_file.write(text + '\n')

