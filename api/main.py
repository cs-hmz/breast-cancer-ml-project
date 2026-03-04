import sys
import os

# Ajouter le dossier parent au path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi import FastAPI
from pydantic import BaseModel
from scripts.predict import predict

app = FastAPI()

class PatientData(BaseModel):
    features: list[float]

@app.post("/predict")
def get_prediction(data: PatientData):
    result = predict(data.features)
    return {"diagnosis": result}
