# https://github.com/rupin01-uni/Syd124Python2nd

import spacy
import time
from transformers import BertTokenizer, BertForTokenClassification
import torch

def extract_entities_spacy(text, nlp_model, max_tokens=2000):
    start_time = time.time()
    doc = nlp_model(text[:max_tokens])
    entities = []
    for ent in doc.ents:
        entities.append((ent.text, ent.label_))
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution Time (spaCy): {execution_time:.2f} seconds")
    return entities

def extract_entities_biobert(text, tokenizer, model, max_tokens=2000):
    start_time = time.time()
    tokens = tokenizer.tokenize(tokenizer.decode(tokenizer.encode(text[:max_tokens])))
    chunk_size = 512
    token_chunks = [tokens[i:i + chunk_size] for i in range(0, len(tokens), chunk_size)]
    entities = []
    for chunk in token_chunks:
        inputs = tokenizer.encode_plus(" ".join(chunk), return_tensors="pt", truncation=True)
        outputs = model(inputs["input_ids"]).logits
        predictions = torch.argmax(outputs, dim=2)
        current_entity = []
        for token, prediction in zip(chunk, predictions[0].numpy()):
            if prediction != 0:
                current_entity.append(token)
            elif current_entity:
                entities.append((" ".join(current_entity), str(prediction)))
                current_entity = []
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution Time (BioBERT): {execution_time:.2f} seconds")
    return entities

if __name__ == "__main__":
    nlp_sci_sm = spacy.load("en_core_sci_sm")
    tokenizer = BertTokenizer.from_pretrained("monologg/biobert_v1.1_pubmed")
    model = BertForTokenClassification.from_pretrained("monologg/biobert_v1.1_pubmed")
    output_txt_file_path = "output_text_file.txt"

    try:
        with open(output_txt_file_path, 'r', encoding='utf-8') as txt_file:
            text_content = txt_file.read()
    except FileNotFoundError:
        print(f"Error: File not found - {output_txt_file_path}")
        exit()

    entities_sci_sm = extract_entities_spacy(text_content, nlp_sci_sm)
    entities_biobert = extract_entities_biobert(text_content, tokenizer, model)

    print("\nTotal Entities Detected by en_core_sci_sm:", len(entities_sci_sm))
    print("\nEntities Detected by en_core_sci_sm:")
    for entity in entities_sci_sm:
        print(entity)

    print("\nTotal Entities Detected by BioBERT:", len(entities_biobert))
    print("\nEntities Detected by BioBERT:")
    for entity in entities_biobert:
        print(entity)
