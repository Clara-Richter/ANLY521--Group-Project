# MedEase
MedEase is a tool that uses NLP to help users better understand medical text. This project is designed to help the average person who does not have strong medical knowledge understand medical text such as discharge notes, medical transcriptions, or any other type of medical text. MedEase is built using Python code and a Dash website.

## Installation
To use this project, you must first create a Conda environment with the required packages. You can do this using the following command:
```
conda env create -f environment.yml
```

This will create a new Conda environment called '...' with all the required packages.

Next, activate the Conda environment using the following command
```
conda activate ...
```

Install MedEase:
```
pip install .
```

Finally, run the following command to launch the Dash website:
```
python dash/nlp_dash.py
```

This will launch the website, which you can access in your web browser by navigating to http://localhost:8050.

## Usage
Once you are on the website, you can input medical text into the text box provided. You can then choose from the following options:

Summarize: This option will generate a summary of the text you provided.  
Label Entities: This option will label medical name entities in the text you provided.  
Definitions: This option will provide definitions for medical terms found in the text you provided.  

"add screenshots of examples here"


