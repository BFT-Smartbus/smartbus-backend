from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import json
import jwt



app = Flask(__name__)
bcrypt = Bcrypt(app)
SECRET_KEY = 'DSDYWIDNFDE'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
with app.app_context():
    db.create_all()

class Users(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(100))
  password = db.Column(db.String(100))

# @app.route("/")
# def home():
#     todo_list = Todo.query.all()
#     return render_template('base.html', todo_list=todo_list)

@app.route('/driverLogin', methods=['POST'])
def login():
      data = json.loads(request.get_data())
      if not data['username'] or not data['password']:
        return "Please enter the required fields", 400
      driver_login = Users.query.filter_by(username=data['username']).first()
      print(driver_login.username)
      hashed_password = driver_login.password
      # if not bcrypt.check_password_hash(hashed_password, data['password']):
      #   return "password you enter is not correct", 400
      # else:
      encoded_jwt = jwt.encode({'username': data['username']}, SECRET_KEY, algorithm="HS256")
        # print(encoded_jwt)
      return encoded_jwt
      # return data
@app.route('riderLogin',methods=['POST'])


if __name__ == "__main__":

  app.run(debug=True)
