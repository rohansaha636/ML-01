import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib
import os

# Load dataset (collegePlace.csv should be in same folder)
data = pd.read_csv("collegePlace.csv")

data.columns = data.columns.str.strip()

# Features (X) and Target (y)
X = data[["Internships", "CGPA"]]
y = data["PlacedOrNot"]

# Train model
model = LogisticRegression()
model.fit(X, y)

# Ensure "models" folder exists
os.makedirs("models", exist_ok=True)

# Save model
model_path = os.path.join("models", "student_model.pkl")
joblib.dump(model, model_path)

print(f"✅ Model saved at {model_path}")
