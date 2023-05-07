import scispacy 
import spacy 
import re

def extract_entities(text):
    '''
    Take medical text and output entities 
    from the text related to disease or chemicals.
    '''
    # remove the puncuation
    text = re.sub(r'[^\w\s]', '', text)
    # change to lower case
    text = text.lower()
    nlp = spacy.load('en_ner_bc5cdr_md')
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents if ent.label_ in ['DISEASE', 'CHEMICAL']]
    return entities