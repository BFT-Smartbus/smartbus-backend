import json
import jwt
from flask import request, Blueprint, jsonify
from modals.Drivers import Users
from config import SECRET_KEY

driver_route = Blueprint("driver_route", __name__)


@driver_route.route("/driverroute", methods=["GET"])
def driveroutes():
    if not request.headers.get("Authorization"):
        return "Please enter the required fields", 401

    # auth_token = request.headers.get("Authorization").split(" ")[1]
    auth_token = request.headers.get("Authorization")

    try:
        driver_entered_data = jwt.decode(auth_token, SECRET_KEY, algorithms="HS256")
        current_logged_in_user = Users.query.filter_by(
            username=driver_entered_data["username"]
        ).first()

        print(current_logged_in_user.username)

        return "some route info", 200

        # return jsonify(current_logged_in_user)

    except:
        return "Token is invalid", 401
