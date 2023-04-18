import spacy


def extract_entities(text):
    print("1")
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]# if ent.label_ in ['DISEASE', 'SYMPTOM', 'TREATMENT']]
    print(entities)
    return entities
