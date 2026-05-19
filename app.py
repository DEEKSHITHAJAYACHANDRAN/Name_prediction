from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI(title="ML Model API")

model = joblib.load("model.pkl")

class InputData(BaseModel):
    features: list

@app.post("/predict")
def predict(data: InputData):
    prediction = model.predict([data.features])
    return {"prediction": int(prediction[0])}

