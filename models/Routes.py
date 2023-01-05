from config import db
import enum
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
# from sqlalchemy import Enum
STRING_SIZE = 2048

class Status(enum.Enum):
    WAITING = "waiting"
    PICKED_UP = "picked_up"
    DROPPED_OFF = "dropped_off"

class Routes(db.Model):
    routeId = db.Column(db.String, primary_key=True)
    timestamp = db.Column(db.Integer,nullable=False)
    duration = db.Column(db.Integer,nullable=False)
    status = db.Column(sqlalchemy.types.Enum(Status),nullable=False)
    polyline = db.Column(db.String(STRING_SIZE),nullable=False)
