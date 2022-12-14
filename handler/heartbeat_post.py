import json
from flask import request, Blueprint
from modals.Heartbeat import Heartbeat
from config import  db

heartbeat_post = Blueprint('heartbeat_post', __name__)

@heartbeat_post.route('/heartbeatpost', methods=['POST'])
def heartbeatpost():
      data = json.loads(request.get_data())
      
      heartbeat_recrod = Heartbeat(user_id=data['user_id'],user_role=data['user_role'],time_stamp=data['time_stamp'],latitude=data['latitude'],longitude=data['longitude'],speed=data['speed'])

      db.session.add(heartbeat_recrod)
      db.session.commit()
      # heartbeat_table = Heartbeat.query.all()
      # return json.dumps({
      #   "uid": heartbeat_recrod.user_id,
      #   "userRole": heartbeat_recrod.user_role,
      #   "time_stamp": heartbeat_recrod.time_stamp,
      #   "latitude": heartbeat_recrod.latitude,
      #   "longitude": heartbeat_recrod.longitude,
      #   "speed": heartbeat_recrod.speed
      # })
      return "heartbeat data added successfully", 200
