import pandas as pd
from evidently.dashboard import Dashboard
from evidently.dashboard.tabs import DataDriftTab
import os

def load_data(train_path, prod_path):
    # Load training and production data
    train_data = pd.read_csv(train_path)
    prod_data = pd.read_csv(prod_path)
    return train_data, prod_data

def monitor_drift(train_data, prod_data):
    dashboard = Dashboard(tabs=[DataDriftTab()])
    dashboard.calculate(train_data, prod_data)
    dashboard.save("drift_report.html")

if __name__ == "__main__":
    train_path = os.getenv("TRAIN_DATA_PATH", "data/winequality-red.csv")
    prod_path = os.getenv("PROD_DATA_PATH", "data/winequality-prod.csv")  # Simulated production data
    train_data, prod_data = load_data(train_path, prod_path)
    monitor_drift(train_data, prod_data)
