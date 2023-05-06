# main
# https://spacy.io/api/top-level#spacy.load
# pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.4.0/en_ner_bc5cdr_md-0.4.0.tar.gz
import argparse
import spacy
from Code.utils.load import load_text
from Code.utils.display import display_entities
from Code.entities import extract_entities
# from Code.summarization import SumText

def main(input_dir):
    # Load text data
    text = load_text(input_dir)
    ent_txt = extract_entities(text)
    # display
    display_entities(text)

    # sum_list = []
    # def_list = []
    # for row in df['transcription']:
    #     res = SumText(row)
    #     res = res.summarize()
    #     res_def = SumText.add_definitions(res)
    #     sum_list.append(res)
    #     def_list.append(res_def)
    # df['summary'] = sum_list
    # df['summary_definitions'] = def_list


        
if __name__ == '__main__':
    # Set up argparse
    parser = argparse.ArgumentParser(description='understand medical documents.')
    parser.add_argument("-f", "--indir", required=True, help='Path to input file')
    #### add add_argument(s) to specify summarization, definitions, entities, NER
    args = parser.parse_args()

    # Call main function with input directory as argument
    main(args.indir)

# call like this: python3 Code/bin/main.py --indir Data/test_text.txt

