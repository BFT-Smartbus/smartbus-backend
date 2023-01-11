from config import db
from dataclasses import dataclass


@dataclass
class Routes(db.Model):
    routeId: str = db.Column(db.String, primary_key=True)
    timestamp: int = db.Column(db.Integer, nullable=False)
    duration: int = db.Column(db.Integer, nullable=False)
    status: str = db.Column(db.String, nullable=False)
    polyline: str = db.Column(db.Text, nullable=False)
