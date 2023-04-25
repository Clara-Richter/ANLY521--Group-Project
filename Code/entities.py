import scispacy
import spacy
#from spacy import display

def extract_entities(text):
    nlp = spacy.load('en_ner_bc5cdr_md')
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents] # if ent.label_ in ['DISEASE', 'SYMPTOM', 'TREATMENT']]
    return entities
    

def display_entities(text):
    nlp = spacy.load('en_ner_bc5cdr_md')
    doc = nlp(text)
    html_doc = spacy.displacy.render(doc, style='ent')
    return html_doc
