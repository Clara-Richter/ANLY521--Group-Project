# main

import argparse
from utils.cleaning import cleaning

def main(input_dir):
    # Load data into a pandas DataFrame
    df= cleaning(input_dir)
    print(df.head())
        
if __name__ == '__main__':
    # Set up argparse
    parser = argparse.ArgumentParser(description='understand medical documents.')
    parser.add_argument("-f", "--indir", required=True, help='Path to input directory')
    args = parser.parse_args()

    # Call main function with input directory as argument
    main(args.indir)

# call like this: python3 Code/bin/main.py --indir Data/mtsamples.csv