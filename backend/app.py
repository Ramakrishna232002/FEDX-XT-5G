from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import numpy as np

from model_handler import ModelHandler

app = FastAPI(title="NEXUS Sentinel API", description="5G Intrusion Detection API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model_handler = ModelHandler()

class PredictRequest(BaseModel):
    features: List[float]

class PredictResponse(BaseModel):
    prediction: int
    prediction_label: str
    confidence: float
    attack_category: str
    attack_description: str
    network_health: str
    network_health_icon: str
    top_features: List[str]
    shap_explanation: dict

@app.get("/")
def root():
    return {"message": "NEXUS Sentinel API", "status": "running"}

@app.get("/health")
def health():
    return {"status": "healthy", "model_loaded": model_handler.is_loaded()}

@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    if len(request.features) != 34:
        raise HTTPException(status_code=400, detail=f"Expected 34 features, got {len(request.features)}")
    
    features = np.array(request.features).reshape(1, -1)
    result = model_handler.predict(features)
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)