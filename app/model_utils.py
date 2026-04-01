import pickle
import numpy as np
import os
import logging

with open('arr_proj_back/models/sal_model.pkl', "rb") as f:
    model = pickle.load(f)

logging.info("ML model loaded successfully")


def predict_salary(experience):
    logging.info(f"Prediction requested for: {experience}")

    prediction = model.predict(np.array([[experience]]))

    logging.info(f"Prediction result: {prediction[0]}")

    return prediction[0]