from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas.predict import PlacementRequest, PlacementResponse
from app.services.predictor import predict_placement

app = FastAPI()

# Allow frontend (React) to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change "*" to frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Placement Predictor API is running"}

@app.post("/predict", response_model=PlacementResponse)
def predict(data: PlacementRequest):
    result = predict_placement(data.cgpa, data.iq)
    return {"placement": result}
