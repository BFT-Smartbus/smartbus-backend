from config import db
import enum
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from dataclasses import dataclass

STRING_SIZE = 2048

class Status(enum.Enum):
    WAITING = "waiting"
    PICKED_UP = "picked_up"
    DROPPED_OFF = "dropped_off"

@dataclass
class Routes(db.Model):
    routeId: str = db.Column(db.String, primary_key=True)
    timestamp: int = db.Column(db.Integer,nullable=False)
    duration: int = db.Column(db.Integer,nullable=False)
    status: Status = db.Column(sqlalchemy.types.Enum(Status))
    polyline: str = db.Column(db.String(STRING_SIZE),nullable=False)
