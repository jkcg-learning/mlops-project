import pandas as pd

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    # Example preprocessing step: Fill missing values
    df = df.fillna(0)
    return df
