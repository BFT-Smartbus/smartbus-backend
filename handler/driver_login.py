import json
import jwt
from flask import request, Blueprint

# from app import app
from modals.Drivers import Users
from config import SECRET_KEY

driver_login = Blueprint("driver_login", __name__)


@driver_login.route("/driverLogin", methods=["POST"])
def driverlogin():
    data = json.loads(request.get_data())
    if not data["username"] or not data["password"]:
        return "Please enter the required fields", 400
    driver_login = Users.query.filter_by(username=data["username"]).first()
    hashed_password = driver_login.password
    # if not bcrypt.check_password_hash(hashed_password, data['password']):
    #   return "password you enter is not correct", 400
    # else:
    encoded_jwt = jwt.encode(
        {"username": data["username"]}, SECRET_KEY, algorithm="HS256"
    )
    # print(encoded_jwt)
    return encoded_jwt
    # return data
