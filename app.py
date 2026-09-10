from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "application": "student-ml-api",
        "version": "1.0.0",
    }


class PredictRequest(BaseModel):
    value: int


@app.post("/predict")
def predict(request: PredictRequest):
    return {
        "input": request.value,
        "prediction": request.value * 2,
    }
