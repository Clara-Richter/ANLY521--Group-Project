import spacy
from spacy import displacy


def display_entities(df):
    nlp = spacy.load('en_core_web_sm')
    for i, row in df.iterrows():
        text = row['transcription']
        entities = row['entities']
        doc = nlp(text)
        displacy.render(doc, style='ent', jupyter=True)
        print(f'Entities: {entities}\n')
