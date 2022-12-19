import os
import json
import jwt
from flask import request, Blueprint
from modals.Drivers import Drivers
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

driver_route = Blueprint("driver_route", __name__)


@driver_route.route("/driver-route", methods=["GET"])
def driveroutes():
    if not request.headers.get("Authorization"):
        return "Please enter the required fields", 401

    # auth_token = request.headers.get("Authorization").split(" ")[1]
    auth_token = request.headers.get("Authorization")

    try:
        driver_entered_data = jwt.decode(auth_token, SECRET_KEY, algorithms="HS256")
        current_logged_in_user = Drivers.query.filter_by(
            username=driver_entered_data["username"]
        ).first()

        return "some route info", 200

    except:
        return "Token is invalid", 401
