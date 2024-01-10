

import spacy
import scispacy
import en_core_sci_sm
from transformers import AutoTokenizer

spacy_model = spacy.load('en_core_sci_sm')

biobert_tokenizer = AutoTokenizer.from_pretrained('monologg/biobert_v1.1_pubmed')




