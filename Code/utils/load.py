# load

from pathlib import Path

def load_text(file_path):
    '''
    Read a text file path and return the whole text.
    '''
    path_file = Path(file_path)

    # logging
    print('Initializing MedEase package...')
    print(f'Importing file from {path_file}')

    # Open a file: file
    file = open(file_path,mode='r')
    # read all lines at once
    text = file.read()

    lines = text.split('\n')
    num_lines = len(lines)

    # logging
    print(f'There are {num_lines} medical texts in the data file.')

    return text