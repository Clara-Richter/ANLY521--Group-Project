import spacy
from spacy import displacy
import re

def display_entities(text):
    # remove the puncuation
    text = re.sub(r'[^\w\s]', '', text)
    # change to lower case
    text = text.lower()
    nlp = spacy.load('en_ner_bc5cdr_md')
    # create a spaCy Doc object from text
    doc = nlp(text)
    entities = [(ent.text, ent.label_, ent.start_char, ent.end_char) for ent in doc.ents if ent.label_ in ['DISEASE', 'CHEMICAL']]
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
                "DISEASE": "#29abd9ff",
                "CHEMICAL": "#95f9eaff"
            }

        html = displacy.render(doc, style="ent", options={"compact": True, "colors": colors})
        

        # save HTML to file
        with open(f"output.html", "w") as f:
            f.write(html)