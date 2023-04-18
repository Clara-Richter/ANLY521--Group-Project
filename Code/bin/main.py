# main
# https://spacy.io/api/top-level#spacy.load
# pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.4.0/en_ner_bc5cdr_md-0.4.0.tar.gz
import argparse
import spacy
from Code.utils.cleaning import cleaning
# from Code.utils.display import display_entities
# from Code.eval.eval import evaluate_model
from Code.entities import extract_entities

def main(input_dir):
    # Load data into a pandas DataFrame
    df = cleaning(input_dir)
    print(df.head())

    # evaluate
    df['entities'] = df['transcription'].apply(extract_entities)
    # evaluate_model(df)

    # # display
    # display_entities(df)


    # call entity ruler model in NER_model.py
    # ruler_model = ...
    # ruler_model.to_disk('./model/ruler_model')

    # call GenerateDataset class to generate annotated text dataset

    # divide subsets for model training, validation, and testing

    
        
if __name__ == '__main__':
    # Set up argparse
    parser = argparse.ArgumentParser(description='understand medical documents.')
    parser.add_argument("-f", "--indir", required=True, help='Path to input file')
    args = parser.parse_args()

    # Call main function with input directory as argument
    main(args.indir)

# call like this: python3 Code/bin/main.py --indir Data/mtsamples.csv