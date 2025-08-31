import joblib
import numpy as np

# Load model once
model = joblib.load("app/models/model2005.pkl")

def predict_placement(cgpa: float, internship: int) -> str:
    X = np.array([[cgpa, internship]])
    prediction = model.predict(X)[0]
    return "Yes" if prediction == 1 else "No"
