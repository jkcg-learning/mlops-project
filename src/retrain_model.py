import pandas as pd
import mlflow
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import os

def load_data(file_path):
    # Load new data for retraining
    data = pd.read_csv(file_path)
    print(f"Columns in the dataset: {data.columns}")
    return data

def preprocess_data(data):
    # Preprocess the data
    data = data.dropna()
    return data

def train_model(data):
    if 'quality' not in data.columns:
        raise KeyError("The 'quality' column is not present in the dataset")
        
    X = data.drop('quality', axis=1)
    y = data['quality']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    mlflow.log_metric('accuracy', accuracy)
    
    mlflow.sklearn.log_model(model, "model")
    return model

if __name__ == "__main__":
    mlflow.start_run()
    data_path = os.getenv("DATA_PATH", "data/winequality-prod.csv")
    data = load_data(data_path)
    data = preprocess_data(data)
    model = train_model(data)
    mlflow.end_run()
