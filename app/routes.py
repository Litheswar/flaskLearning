from flask import Blueprint, request, jsonify, render_template
from app.model_utils import predict_salary
import logging
import os

routes = Blueprint('routes', __name__)

@routes.route("/")
def home():
    logging.info("Home route accessed")
    return render_template("index.html")  # ✅ fixed name

@routes.route("/test")
def test():
    logging.debug("Test route accessed")
    return "Test successful"

@routes.route("/predict", methods=['POST'])
def predict():

    logging.info("Prediction route accessed")

    API_KEY = os.getenv("API_KEY")

    data = request.get_json()
    user_key = request.headers.get("x-api-key")

    print("ENV API_KEY:", API_KEY)
    print("USER KEY:", user_key)

    if user_key != API_KEY:
        logging.warning("Unauthorized access")
        return make_response("fail", "Unauthorized"), 401

    if not data:
        return make_response("fail", "No input data"), 400

    if 'experience' not in data:
        return make_response("fail", "Missing experience"), 400

    # ✅ safer conversion
    try:
        experience = float(data['experience'])
    except ValueError:
        return make_response("fail", "Experience must be a number"), 400

    if experience < 0:
        return make_response("fail", "Invalid value"), 400

    prediction = predict_salary(experience)

    return make_response("success", "Prediction successful", {
        "prediction": prediction
    })


def make_response(status, message, data=None):
    return jsonify({
        "status": status,
        "message": message,
        "data": data
    })
