from flask import Flask, jsonify
import logging
from app.routes import routes
from dotenv import load_dotenv
import os

def create_app():
    load_dotenv()
    app=Flask(__name__)
    API_KEY = os.getenv("API_KEY")
    logging.basicConfig(filename='arr_proj_back/logs/apps.log',
                        level = logging.DEBUG,
                        format='%(asctime)s  -  %(levelname)s  -  %(message)s')
    app.register_blueprint(routes)
    
    # GLoBAL error handler
    @app.errorhandler(Exception)
    def handle_exception(e):
        logging.error(f"Unhandled Exception: {e}")
        
        return jsonify({
            "status": "fail",
            "message": str(e),
            "data": None
        }), 500
        
    # ✅ SPECIFIC ERROR HANDLER
    @app.errorhandler(ValueError)
    def handle_value_error(e):
        logging.warning(f"Value Error: {e}")

        return jsonify({
            "status": "fail",
            "message": "Invalid input type",
            "data": None
        }), 400
        
    
    return app

