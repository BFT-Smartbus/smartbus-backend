from config import db

class Heartbeat(db.Model):
  heartbeat_id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  user_role = db.Column(db.String(100))
  time_stamp = db.Column(db.Integer)
  latitude = db.Column(db.Float)
  longitude = db.Column(db.Float)
  speed = db.Column(db.Float)
