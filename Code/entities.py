import spacy

def extract_entities(text):
    nlp = spacy.load('en_ner_bc5cdr_md')
    doc = nlp(text)
    entities = [(ent.text, ent.label_, ent.start_char, ent.end_char) for ent in doc.ents if ent.label_ in ['DISEASE', 'CHEMICAL']]
    return entities
    

def display_entities(text):
    nlp = spacy.load('en_ner_bc5cdr_md')
    doc = nlp(text)
    html_doc = spacy.displacy.render(doc, style='ent')
    return html_doc
