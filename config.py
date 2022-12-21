import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

load_dotenv()
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

SQLALCHEMY_DATABASE_URI = (
    f"postgresql://{USERNAME}:{PASSWORD}@localhost/smartbus_backend"
)

db = SQLAlchemy()
bcrypt = Bcrypt()
