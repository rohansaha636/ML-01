import joblib
import numpy as np

# Load model once
model = joblib.load("app/models/placement_model.pkl")

def predict_placement(cgpa: float, iq: int) -> str:
    X = np.array([[cgpa, iq]])
    prediction = model.predict(X)[0]
    return "Yes" if prediction == 1 else "No"
