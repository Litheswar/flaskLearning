from flask import Blueprint, request, jsonify, render_template
from app.model_utils import predict_salary
import logging
import os


API_KEY = os.getenv("API_KEY")
routes = Blueprint('routes', __name__)

@routes.route("/")
def home():
    logging.info("Home route accessed")
    return render_template("inde.html")

@routes.route("/test")
def test():
    logging.debug("Test route accessed")
    return "Test successful"

# @routes.route("/predict", methods=['POST'])
# def predict():
    
#         try:
#             logging.info("Prediction route accessed")
#             user_key = request.headers.get("x-api-key")

#             data = request.get_json()

#             if API_KEY != user_key:
#                 logging.warning("Unauthorized access attempt with invalid API key")
#                 return make_response("fail", "Unauthorized: Invalid API key"), 401
                
#             if not data:
#                 logging.warning("No JSON data received")
#                 return make_response("fail", "No input data"), 400
            
#             if 'experience' not in data:
#                 logging.warning("Experience key missing in input data")
#                 return make_response("fail", "Missing 'experience' key"), 400
            
#             experience = float(data['experience'])
#             logging.info(f"Received experience: {experience}")
        
#             if experience < 0:
#                 logging.warning("Negative experience given")
#                 return make_response("fail", "Experience cannot be negative"), 400

#             prediction = predict_salary(experience)

#             return make_response("success", "Prediction successful", {
#                 "prediction": prediction
#             })

#         except Exception as e:
#             logging.error(f"Error in /predict: {e}")

#             return make_response("fail", "An error occurred during prediction"), 500    
         
         
@routes.route("/predict", methods=['POST'])
def predict():

    logging.info("Prediction route accessed")

    data = request.get_json()

    user_key = request.headers.get("x-api-key")

    if user_key != API_KEY:
        logging.warning("Unauthorized access")
        return make_response("fail", "Unauthorized"), 401

    if not data:
        return make_response("fail", "No input data"), 400

    if 'experience' not in data:
        return make_response("fail", "Missing experience"), 400

    experience = float(data['experience'])

    if experience < 0:
        return make_response("fail", "Invalid value"), 400

    prediction = predict_salary(experience)

    return make_response("success", "Prediction successful", {
        "prediction": prediction
    })
   
def make_response(status, message, data=None):
    return jsonify({
        "status":status,
        "message": message,
        "data":data
    })