import json
import jwt
import config
import os
from dotenv import load_dotenv
from flask import Flask, request
from config import db
from models.Drivers import Drivers
from models.Riders import Riders

# os, dotenv, and load_dotenv() are what we need to use .env to hide confidential code
load_dotenv()
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

app = Flask(__name__)

app.config.from_object(config)
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/driver-login", methods=["POST"])
def driver_login():
    data = json.loads(request.get_data())
    if not data["username"] or not data["password"]:
        return "Please enter the required fields", 400

    return return_jwt_to_user(data, Drivers)


@app.route("/rider-login", methods=["POST"])
def rider_login():
    data = json.loads(request.get_data())
    if not data["username"] or not data["password"]:
        return "Please enter the required fields", 400

    return return_jwt_to_user(data, Riders)


@app.route("/driver-route", methods=["GET"])
def get_driver_routes():
    if not request.headers.get("Authorization"):
        return "Please enter the required fields", 401

    auth_token = request.headers.get("Authorization")

    return handle_driver_authentication(auth_token)


if __name__ == "__main__":

    app.run(debug=True)

# helper functions
def return_jwt_to_user(data, role):
    username_from_frontend = data["username"]
    driver_login = role.query.filter_by(username=username_from_frontend).first()
    encoded_jwt = jwt.encode(
        {"username": username_from_frontend}, JWT_SECRET_KEY, algorithm="HS256"
    )
    return encoded_jwt


def handle_driver_authentication(auth_token):
    try:
        driver_entered_data = jwt.decode(auth_token, JWT_SECRET_KEY, algorithms="HS256")
        driver_username = driver_entered_data["username"]
        current_logged_in_user = Drivers.query.filter_by(
            username=driver_username
        ).first()

        return "some route info to display when driver logs in", 200

    except:
        return "Token is invalid", 401
