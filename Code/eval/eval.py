# eval
import pandas as pd 
import nltk
import spacy
from Code.entities import extract_entities
from sklearn.metrics import precision_score, recall_score, f1_score

def evaluate_model(df):
    true_positives = 0
    false_positives = 0
    false_negatives = 0

    for i, row in df.iterrows():
        text = row['transcription']
        true_entities = set(row['entities'])
        predicted_entities = set(extract_entities(text))

        for entity in predicted_entities:
            if entity in true_entities:
                true_positives += 1
            else:
                false_positives += 1

        for entity in true_entities:
            if entity not in predicted_entities:
                false_negatives += 1

    precision = true_positives / (true_positives + false_positives)
    recall = true_positives / (true_positives + false_negatives)
    f1 = 2 * (precision * recall) / (precision + recall)

    print(f'Precision: {precision:.2f}')
    print(f'Recall: {recall:.2f}')
    print(f'F1 Score: {f1:.2f}')

    