from omegaconf import OmegaConf
from data_loader import load_data
from preprocess import preprocess_data
from model import train_model
from schema import data_schema

def main():
    config = OmegaConf.load('src/config.yaml')

    df = load_data(config.data.path)
    df = preprocess_data(df)

    # Validate data schema
    data_schema.validate(df)

    train_model(df, config.model.params)
    print("Model trained and logged with MLflow")

if __name__ == "__main__":
    main()
