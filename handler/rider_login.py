import os
import json
import jwt
from flask import request, Blueprint
from modals.Riders import Riders
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

rider_login = Blueprint("rider_login", __name__)


@rider_login.route("/rider-login", methods=["POST"])
def riderLogin():
    data = json.loads(request.get_data())
    if not data["username"] or not data["password"]:
        return "Please enter the required fields", 400
    rider_login = Riders.query.filter_by(username=data["username"]).first()
    print(rider_login)
    hashed_password = rider_login.password
    encoded_jwt = jwt.encode(
        {"username": data["username"]}, SECRET_KEY, algorithm="HS256"
    )
    return encoded_jwt
