import os
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv

load_dotenv()
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")


SQLALCHEMY_DATABASE_URI = (
    f"postgresql://{USERNAME}:{PASSWORD}@localhost/smartbus_backend"
)
SQLALCHEMY_TRACK_MODIFICATIONS = False

db = SQLAlchemy()
bcrypt = Bcrypt()
