import spacy
from spacy.lang.en import English
from spacy.pipeline import EntityRuler

class RulerModel():
    def __init__(self, surgery, internalMedicine, medication, obstetricsGynecology):
        self.ruler_model = spacy.blank('en')
        self.entity_ruler =      self.ruler_model.add_pipe('entity_ruler')
        
        total_patterns = []
        patterns = self.create_patterns(surgery, 'surgery')
        total_patterns.extend(patterns)
        patterns = self.create_patterns(internalMedicine, 'internalMedicine')
        total_patterns.extend(patterns)
        patterns = self.create_patterns(medication, 'medication')
        total_patterns.extend(patterns)
 
        patterns = self.create_patterns(obstetricsGynecology, 'obstetricsGynecology')
        total_patterns.extend(patterns)
        
        self.add_patterns_into_ruler(total_patterns)
        
        self.save_ruler_model()
        
    def create_patterns(self, entity_type_set, entity_type):
        patterns = []
        for item in entity_type_set:
            pattern = {'label': entity_type, 'pattern': item}
            patterns.append(pattern)
        return patterns
    
    def add_patterns_into_ruler(self, total_patterns):
        self.entity_ruler.add_patterns(total_patterns)


# annotated text dataset
class GenerateDataset(object):
    
    def __init__(self, ruler_model):
        self.ruler_model = ruler_model
        
    def find_entitytypes(self, text):
        ents = [] 
        doc = self.ruler_model(str(text))
        for ent in doc.ents:
            ents.append((ent.start_char, ent.end_char, ent.label_))
        return ents     
    
    def assign_labels_to_documents(self, df):
        dataset = []
        text_list = df['transcription'].values.tolist()
        for text in text_list:
            ents = self.find_entitytypes(text)
            if len(ents) > 0:
                dataset.append((text, {'entities': ents}))
            else:
                continue 
        return dataset





