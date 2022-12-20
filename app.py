import json
import jwt
import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv

# os, dotenv, and load_dotenv() are what we need to use .env to hide confidential code

load_dotenv()
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")


app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"postgresql://{USERNAME}:{PASSWORD}@localhost/smartbus_backend"
db = SQLAlchemy(app)

bcrypt = Bcrypt()


class Drivers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))


class Riders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))


with app.app_context():
    db.create_all()


@app.route("/driver-login", methods=["POST"])
def driverlogin():
    data = json.loads(request.get_data())
    if not data["username"] or not data["password"]:
        return "Please enter the required fields", 400
    driver_login = Drivers.query.filter_by(username=data["username"]).first()
    # hashed_password = driver_login.password
    # if not bcrypt.check_password_hash(hashed_password, data['password']):
    #   return "password you enter is not correct", 400
    # else:
    encoded_jwt = jwt.encode(
        {"username": data["username"]}, JWT_SECRET_KEY, algorithm="HS256"
    )
    return encoded_jwt


@app.route("/rider-login", methods=["POST"])
def riderLogin():
    data = json.loads(request.get_data())
    if not data["username"] or not data["password"]:
        return "Please enter the required fields", 400
    rider_login = Riders.query.filter_by(username=data["username"]).first()
    hashed_password = rider_login.password
    encoded_jwt = jwt.encode(
        {"username": data["username"]}, JWT_SECRET_KEY, algorithm="HS256"
    )
    return encoded_jwt


@app.route("/driver-route", methods=["GET"])
def driveroutes():
    if not request.headers.get("Authorization"):
        return "Please enter the required fields", 401

    # auth_token = request.headers.get("Authorization").split(" ")[1]
    auth_token = request.headers.get("Authorization")

    try:
        driver_entered_data = jwt.decode(auth_token, JWT_SECRET_KEY, algorithms="HS256")
        current_logged_in_user = Drivers.query.filter_by(
            username=driver_entered_data["username"]
        ).first()

        return "some route info", 200

    except:
        return "Token is invalid", 401


if __name__ == "__main__":

    app.run(debug=True)
