# import scispacy
"""import spacy 

# def extract_entities(text):
#     #print(text)
#     #nlp = spacy.load('en-core-sci-sm')
#     nlp = spacy.load('en_ner_bc5cdr_md')
#     doc = nlp(text)
#     #entities = doc.ents
#     entities = [(ent.text, ent.label_) for ent in doc.ents if ent.label_ in ['DISEASE', 'SYMPTOM', 'TREATMENT']]
#     return entities


# text = "The patient is well known to me for a history of iron-deficiency anemia due to chronic blood loss from colitis.  We corrected her hematocrit last year with intravenous (IV) iron.  Ultimately, she had a total proctocolectomy done on 03/14/2007 to treat her colitis.  Her course has been very complicated since then with needing multiple surgeries for removal of hematoma.  This is partly because she was on anticoagulation for a right arm deep venous thrombosis (DVT) she had early this year, complicated by septic phlebitis.,Chart was reviewed, and I will not reiterate her complex history.,I am asked to see the patient again because of concerns for coagulopathy.,She had surgery again last month to evacuate a pelvic hematoma, and was found to have vancomycin resistant enterococcus, for which she is on multiple antibiotics and followed by infectious disease now.,She is on total parenteral nutrition (TPN) as well.,LABORATORY DATA:,  Labs today showed a white blood "
# print(extract_entities(text))


# cleaning

import re
import os.path
import pandas as pd
import numpy as np
from pathlib import Path

# drop rows with na transcription
def cleaning(file_path):
    path_file = Path(file_path)
    df = pd.read_csv(path_file, index_col=0)
    df.dropna(subset=['transcription'], inplace=True) # drop rows with missing transcripts
    # remove the “.,” marks that appear to separate some sections of the transcription
    df['transcription'] = df['transcription'].apply(lambda x: re.sub('(\.,)', ". ", x))
    # change the transcriptions column to lower case
    df['transcription'] = df['transcription'].str.lower()
    df = df.sample(n=50, replace=False, random_state=42)
    data_path = Path(path_file.parent, 'small_clean_data.csv')
    # save cleaned data
    df.to_csv(data_path, index=False)
    return df

file_path = 'Data/mtsamples.csv'
cleaning(file_path)

"""

import spacy 
from spacy import displacy
import json

# assume you have a Doccano project with annotations
# create a list of annotations in Doccano format
annotations = [
    {"text": "heart attack", "start_offset": 0, "end_offset": 11, "label": "PROBLEM"},
    {"text": "aspirin", "start_offset": 20, "end_offset": 27, "label": "TREATMENT"},
    {"text": "high blood pressure", "start_offset": 42, "end_offset": 61, "label": "PROBLEM"},
    {"text": "lisinopril", "start_offset": 66, "end_offset": 76, "label": "TREATMENT"}
]

# create a spaCy Doc object from text
text = "The patient was admitted with a history of heart attack. He was prescribed aspirin and lisinopril to manage his high blood pressure."
nlp = spacy.load('en_ner_bc5cdr_md')
doc = nlp(text)

# add entities to the Doc object
for annotation in annotations:
    start_offset = annotation["start_offset"]
    end_offset = annotation["end_offset"]
    label = annotation["label"]
    span = doc.char_span(start_offset, end_offset, label=label)
    if span is not None:
        doc.ents = list(doc.ents) + [span]

# generate HTML visualization
html = displacy.render(doc, style="ent", options={"compact": True})

# save HTML to file
with open("output.html", "w") as f:
    f.write(html)
