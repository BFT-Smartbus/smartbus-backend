from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

SECRET_KEY = "DSDYWIDNFDE"
SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite"
SQLALCHEMY_TRACK_MODIFICATIONS = False

db = SQLAlchemy()
bcrypt = Bcrypt()
