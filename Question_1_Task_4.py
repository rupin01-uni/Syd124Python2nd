

NER using en_core_sci_sm
doc_spacy = spacy_model(text)
diseases_spacy = [ent.text for ent in doc_spacy.ents if ent.label_ == 'DISEASE']
drugs_spacy = [ent.text for ent in doc_spacy.ents if ent.label_ == 'CHEMICAL']

# NER using biobert
tokens_biobert = biobert_tokenizer.tokenize(biobert_tokenizer.decode(biobert_tokenizer.encode(text)))
tokens_biobert_str = ' '.join(tokens_biobert)
diseases_biobert = [entity for entity in tokens_biobert_str.split() if 'Disease' in entity]
drugs_biobert = [entity for entity in tokens_biobert_str.split() if 'Drug' in entity]

# Compare the results
total_entities_spacy = len(diseases_spacy) + len(drugs_spacy)
total_entities_biobert = len(diseases_biobert) + len(drugs_biobert)

print(total_entities_spacy)
print(total_entities_biobert)
print(diseases_biobert)
print(drugs_biobert)