import pandas as pd

def load_and_preprocess(path):
    df = pd.read_csv(path)
    df = df.dropna()
    return df
