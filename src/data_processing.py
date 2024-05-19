import pandas as pd
import re

def load_data(save_data=False):
    df_vision = pd.read_excel('src/data/S&P500 vision.xlsx', usecols=[0, 1, 2])
    df_meta = pd.read_csv('src/data/metadata.tsv', sep='\t', header=0)

    # Apply preprocessing to vision data 
    df_vision['Processed'] = df_vision['Value'].apply(preprocess_helper)
    if save_data:
        df_vision.to_excel('src/data/vision_data_processed.xlsx', index=False)

    return df_vision, df_meta

def preprocess_helper(text):
    if not isinstance(text, str):
        text = str(text)
    text = text.lower()
    text = re.sub(r'\b\w{1,3}\b', '', text)  # Remove short words less than 3 characters
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    return text

