# cleaning

import re
import os.path
import pandas as pd
import numpy as np
from pathlib import Path

# drop rows with na transcription
def cleaning(file_path):
    path_file = Path(file_path)
    if os.path.isfile(path_file.parent / 'clean_data.csv'):
        df = pd.read_csv(path_file.parent / 'clean_data.csv')
        return df
    else:
        df = pd.read_csv(path_file)
        df.dropna(subset=['transcription'], inplace=True) # drop rows with missing transcripts
        # remove the “.,” marks that appear to separate some sections of the transcription
        df['transcription'] = df['transcription'].apply(lambda x: re.sub('(\.,)', ". ", x))
        # change the transcriptions column to lower case
        df['transcription'] = df['transcription'].str.lower()

        ############
        df = df.sample(n=2, replace=False, random_state=42)
        ##########

        #### deal with data imbalance issue ?????
        # filtered_data = df[['transcription', 'medical_specialty']]
        # # Mask not medical specialties
        # mask = (filtered_data['medical_specialty'] == 'SOAP / Chart / Progress Notes') | \
        #     (filtered_data['medical_specialty'] == 'Office Notes') | \
        #     (filtered_data['medical_specialty'] == 'Consult - History and Phy.') | \
        #     (filtered_data['medical_specialty'] == 'Emergency Room Reports') | \
        #     (filtered_data['medical_specialty'] == 'Discharge Summary') | \
        #     (filtered_data['medical_specialty'] == 'Letters')
        # filtered_data = filtered_data[~mask]
        # # remove less than 100 data samples
        # data_categories  = filtered_data.groupby(filtered_data['medical_specialty'])
        # filtered_data_categories = data_categories.filter(lambda x:x.shape[0] > 100)
        # df = filtered_data_categories.sample(frac=1.0)

        # determine the path where to save the data file
        data_path = Path(path_file.parent, 'clean_data.csv')
        # save cleaned data
        df.to_csv(data_path, index=False)
        return df
 

# split?
# def split_data(file_path):
#     path_file = Path(file_path)
#     # check if train and test files exist already
#     if os.path.isfile(path_file.parent / 'train.tsv') and os.path.isfile(path_file.parent / 'test.tsv'):
#          pass
#     else:
#         df = pd.read_csv(path_file, sep='\t')
#         ...
#         # determine the path where to save the train and test file
#         train_path = Path(path_file.parent, 'train.tsv')
#         test_path = Path(path_file.parent, 'test.tsv')

#         # save the train and test file
#         train.to_csv(train_path,  index=False)
#         test.to_csv(test_path,  index=False)