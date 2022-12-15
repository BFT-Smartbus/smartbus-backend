import json
from flask import request, Blueprint
from modals.Heartbeat import Heartbeat
from config import  db

heartbeat_post = Blueprint('heartbeat_post', __name__)

@heartbeat_post.route('/heartbeatpost', methods=['POST'])
def heartbeatpost():
      data = json.loads(request.get_data())
      
      heartbeat_record = Heartbeat(
            user_id=data['user_id'],
            user_role=data['user_role'],
            time_stamp=data['time_stamp'],
            latitude=data['latitude'],
            longitude=data['longitude'],
            speed=data['speed'])

      db.session.add(heartbeat_record)
      db.session.commit()

      return "heartbeat data added successfully", 200
