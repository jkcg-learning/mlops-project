import mlflow
import mlflow.pyfunc
from fastapi import FastAPI, HTTPException
import pandas as pd
from pydantic import BaseModel
from prometheus_client import start_http_server, Summary, Counter
import uvicorn

# Define the request body schema
class WineQualityInput(BaseModel):
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float
    total_sulfur_dioxide: float
    density: float
    pH: float
    sulphates: float
    alcohol: float

# Initialize the FastAPI app
app = FastAPI()

# Function to get the latest model
def get_latest_model():
    client = mlflow.tracking.MlflowClient()
    experiments = client.search_experiments()
    latest_run = None
    for experiment in experiments:
        runs = client.search_runs(experiment_ids=[experiment.experiment_id])
        for run in runs:
            if latest_run is None or run.info.start_time > latest_run.info.start_time:
                latest_run = run
    if latest_run:
        model_uri = f"/app/mlruns/{latest_run.info.experiment_id}/{latest_run.info.run_id}/artifacts/model"
        return mlflow.pyfunc.load_model(model_uri)
    else:
        raise Exception("No models found")

# Load the latest model
model = get_latest_model()

# Create Prometheus metrics
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
PREDICTION_COUNT = Counter('prediction_count', 'Number of predictions made')

@app.post("/predict")
@REQUEST_TIME.time()
def predict(input: WineQualityInput):
    try:
        input_df = pd.DataFrame([input.dict()])
        prediction = model.predict(input_df)
        PREDICTION_COUNT.inc()
        return {"quality": prediction[0]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    # Start Prometheus metrics server
    start_http_server(8001)
    uvicorn.run(app, host="0.0.0.0", port=8000)
