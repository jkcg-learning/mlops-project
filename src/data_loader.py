import pandas as pd

def load_data(data_path: str) -> pd.DataFrame:
    df = pd.read_csv(data_path, sep=';')
    return df
