import pandas as pd
from data_models import WineQuality
from pydantic import ValidationError
from loguru import logger

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """Preprocess and validate the data.

    Args:
        df (pd.DataFrame): DataFrame to preprocess.

    Returns:
        pd.DataFrame: Preprocessed and validated DataFrame.

    Raises:
        ValidationError: If data validation fails during preprocessing.
    """
    # Example preprocessing step: Fill missing values
    df = df.fillna(0)

    # Validate data using Pydantic
    try:
        validated_data = [WineQuality(**record) for record in df.to_dict(orient='records')]
        validated_df = pd.DataFrame([item.dict(by_alias=True) for item in validated_data])
        logger.info("Data preprocessed and validated successfully")
        return validated_df
    except ValidationError as e:
        logger.error(f"Data validation error during preprocessing: {e}")
        raise
