from config import db

class Riders(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(100))
  password = db.Column(db.String(100))
  something = db.Column(db.String(100))