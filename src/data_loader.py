import pandas as pd
from pydantic import ValidationError
from data_models import WineQuality
from loguru import logger

def load_data(data_path: str) -> pd.DataFrame:
    """Load and validate data from a CSV file.

    Args:
        data_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Validated DataFrame.

    Raises:
        ValidationError: If data validation fails.
    """
    df = pd.read_csv(data_path, sep=';')

    try:
        validated_data = [WineQuality(**record) for record in df.to_dict(orient='records')]
        validated_df = pd.DataFrame([item.dict(by_alias=True) for item in validated_data])
        logger.info("Data loaded and validated successfully")
        return validated_df
    except ValidationError as e:
        logger.error(f"Data validation error: {e}")
        raise
