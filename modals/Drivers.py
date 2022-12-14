from config import db

class Users(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(100))
  password = db.Column(db.String(100))
  heartbeat = db.relationship('Heartbeat', backref='users', lazy=True)