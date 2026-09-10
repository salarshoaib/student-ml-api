from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "application": "student-ml-api",
        "application_version": "1.1.0",
        "model_version": "model-1",
    }


class PredictRequest(BaseModel):
    value: int


@app.post("/predict")
def predict(request: PredictRequest):
    return {
        "input": request.value,
        "prediction": request.value * 2,
    }
