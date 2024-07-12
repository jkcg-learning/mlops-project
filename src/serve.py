from fastapi import FastAPI, HTTPException
import pandas as pd
from pydantic import BaseModel
import mlflow.pyfunc
import uvicorn
from prometheus_client import start_http_server, Summary, Counter
from datetime import datetime

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

# Load the latest model
model_path = "/app/mlruns/latest_model_path"  # Adjust to point to the latest model
model = mlflow.pyfunc.load_model(model_path)

# Create Prometheus metrics
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
PREDICTION_COUNT = Counter('prediction_count', 'Number of predictions made')

# Logging function
def log_prediction(data, prediction):
    log_entry = data.copy()
    log_entry['prediction'] = prediction
    log_entry['timestamp'] = datetime.utcnow().isoformat()
    log_df = pd.DataFrame([log_entry])
    log_df.to_csv('predictions_log.csv', mode='a', header=False, index=False)

@app.post("/predict")
@REQUEST_TIME.time()
def predict(input: WineQualityInput):
    try:
        input_data = {
            "fixed acidity": input.fixed_acidity,
            "volatile acidity": input.volatile_acidity,
            "citric acid": input.citric_acid,
            "residual sugar": input.residual_sugar,
            "chlorides": input.chlorides,
            "free sulfur dioxide": input.free_sulfur_dioxide,
            "total sulfur dioxide": input.total_sulfur_dioxide,
            "density": input.density,
            "pH": input.pH,
            "sulphates": input.sulphates,
            "alcohol": input.alcohol
        }
        input_df = pd.DataFrame([input_data])
        prediction = model.predict(input_df)
        PREDICTION_COUNT.inc()
        
        # Log prediction
        log_prediction(input_data, prediction[0])
        
        return {"quality": prediction[0]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    # Start Prometheus metrics server
    start_http_server(8001)
    uvicorn.run(app, host="0.0.0.0", port=8000)
