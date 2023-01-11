from dotenv import load_dotenv
from twilio.rest import Client
load_dotenv()
import os
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="ANIME IS AWESOME!",
                     from_= os.environ['FROM_NUMBER'],
                     to= os.environ['TO_NUMBER']
                 )

