import pickle
import numpy as np
import logging
import os

# Correct path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "sal_model.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

logging.info("ML model loaded successfully")


def predict_salary(experience):
    logging.info(f"Prediction requested for: {experience}")

    prediction = model.predict(np.array([[experience]]))

    logging.info(f"Prediction result: {prediction[0]}")

    return float(prediction[0])   # ✅ ensure JSON safe
