import spacy
from spacy import displacy
from IPython.core.display import display, HTML
from pathlib import Path
import json

def display_entities(df):
    nlp = spacy.load('en_ner_bc5cdr_md')
    for i, row in df.iterrows():
        text = row['transcription']
        entities = row['entities']
        # create a spaCy Doc object from text
        doc = nlp(text)
        # add entities to the Doc object
        for entity in entities:
            span = doc.char_span(text.find(entity[0]), text.find(entity[0]) + len(entity[0]), label=entity[1])
            if span is not None:
                # check for overlaps with existing entities
                overlaps = [ent for ent in doc.ents if ent.start < span.end and ent.end > span.start]
                if overlaps:
                    continue
                doc.ents = list(doc.ents) + [span]
            # if span is not None:
            #     doc.ents = list(doc.ents) + [span]

        # generate HTML visualization
        colors = {
                "DISEASE": "#FF5733",
                "SYMPTOM": "#F7DC6F",
                "TREATMENT": "#ABEBC6",
            }

        html = displacy.render(doc, style="ent", options={"compact": True, "colors": colors})
        

        # save HTML to file
        with open(f"output_{i}.html", "w") as f:
            f.write(html)
