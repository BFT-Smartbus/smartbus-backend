import config
import json
import jwt
from flask import Flask, request
from config import db, SECRET_KEY
from modals.Drivers import Users
from modals.Riders import Riders


app = Flask(__name__)
# make app available to fll files within entire folder
app.config.from_object(config)
db.init_app(app)


with app.app_context():
    db.create_all()


@app.route("/driverLogin", methods=["POST"])
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


@app.route("/riderLogin", methods=["POST"])
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


@app.route("/driverroute", methods=["GET"])
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


if __name__ == "__main__":

    app.run(debug=True)
