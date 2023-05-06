# load

from pathlib import Path

def load_text(file_path):
    path_file = Path(file_path)
    # Open a file: file
    file = open(file_path,mode='r')
    # read all lines at once
    text = file.read()
    return text