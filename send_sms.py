from dotenv import load_dotenv
from twilio.rest import Client
load_dotenv()
import os

def SEND_SMS():
  account_sid = os.environ['TWILIO_ACCOUNT_SID']
  auth_token = os.environ['TWILIO_AUTH_TOKEN']
  client = Client(account_sid, auth_token)
  message = client.messages \
                .create(
                     body="ANIME IS AWESOME IT IS OVER 9000!",
                     from_= os.environ['FROM_NUMBER'],
                     to= os.environ['TO_NUMBER']
                 )

SEND_SMS()
