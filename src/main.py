import argparse
from omegaconf import OmegaConf
from loguru import logger
from data_loader import load_data
from preprocess import preprocess_data
from train_model import train_model
from schema import data_schema

def parse_args():
    """Parse command-line arguments.

    Returns:
        argparse.Namespace: Parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Wine Quality Prediction")
    parser.add_argument('--config', type=str, default='src/config.yaml', help='Path to the configuration file')
    return parser.parse_args()

def main():
    """Main function to run the wine quality prediction pipeline."""
    args = parse_args()

    # Load configuration
    config = OmegaConf.load(args.config)
    logger.info(f"Loaded configuration from {args.config}")

    # Load and validate data
    try:
        df = load_data(config.data.path)
        data_schema.validate(df)
        logger.info("Data loaded and validated successfully")
    except Exception as e:
        logger.error(f"Failed to load or validate data: {e}")
        return

    # Preprocess data
    try:
        df = preprocess_data(df)
        logger.info("Data preprocessed successfully")
    except Exception as e:
        logger.error(f"Failed to preprocess data: {e}")
        return

    # Train model
    try:
        train_model(df, config.model.params)
        logger.info("Model trained and logged with MLflow")
    except Exception as e:
        logger.error(f"Failed to train model: {e}")
        return

if __name__ == "__main__":
    logger.add("logs/wine_quality.log", rotation="1 MB")
    main()
