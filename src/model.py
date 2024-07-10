import mlflow
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

def train_model(df: pd.DataFrame, params: dict):
    X = df.drop(columns=["quality"])
    y = df["quality"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    with mlflow.start_run():
        model = RandomForestClassifier(**params)
        model.fit(X_train, y_train)

        mlflow.sklearn.log_model(model, "model")
        mlflow.log_params(params)

        accuracy = model.score(X_test, y_test)
        mlflow.log_metric("accuracy", accuracy)

        return model
