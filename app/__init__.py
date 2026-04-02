from flask import Flask, jsonify
import logging
from app.routes import routes
from dotenv import load_dotenv
import os

def create_app():
    # 🔥 FORCE LOAD .env FROM CORRECT PATH
    BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    env_path = os.path.join(BASE_DIR, ".env")
    load_dotenv(env_path)

    app = Flask(__name__)

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s  -  %(levelname)s  -  %(message)s'
    )

    app.register_blueprint(routes)

    # GLOBAL error handler
    @app.errorhandler(Exception)
    def handle_exception(e):
        logging.error(f"Unhandled Exception: {e}")
        
        return jsonify({
            "status": "fail",
            "message": str(e),
            "data": None
        }), 500
        
    # SPECIFIC ERROR HANDLER
    @app.errorhandler(ValueError)
    def handle_value_error(e):
        logging.warning(f"Value Error: {e}")

        return jsonify({
            "status": "fail",
            "message": "Invalid input type",
            "data": None
        }), 400
        
    return app
