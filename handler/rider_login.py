import json
import jwt
from flask import request, Blueprint

# from app import app
from modals.Riders import Riders
from config import SECRET_KEY

rider_login = Blueprint("rider_login", __name__)


@rider_login.route("/riderLogin", methods=["POST"])
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
