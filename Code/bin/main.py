# main
# https://spacy.io/api/top-level#spacy.load
# pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.4.0/en_ner_bc5cdr_md-0.4.0.tar.gz
import argparse
import spacy
from Code.utils.load import load_text
from Code.utils.display import display_entities
from Code.entities import extract_entities
from Code.summarization import SumText
import webbrowser

def main():
    parser = argparse.ArgumentParser(description='understand medical documents.')
    parser.add_argument("-f", "--indir", required=True, help='Path to input file')
    parser.add_argument("-t", "--type", required=True,
                        choices=["summary", "definitions", "entities", "display"],
                        help='Choose type of simplifier')
    args = parser.parse_args()
    text = load_text(args.indir)
    if args.type == 'summary':
        result = SumText(text)
        result = result.summarize()
        print(result)
    elif args.type == 'definitions':
        result = SumText(text)
        result = result.add_definitions()
        print(result)
    elif args.type == 'entities':
        result = extract_entities(text)
        print(result)
    elif args.type == 'display':
        display_entities(text)


if __name__ == '__main__':
    main()


# call like this: python3 Code/bin/main.py --indir Data/test_text.txt

