import os
from twilio.rest import Client

account_sid = os.environ['ACCOUNT_SID']
auth_token = os.environ['AUTH_TOKEN']
client = Client(account_sid, auth_token)


to = os.environ['my_num']

print("Enter a vaild img url:")
url = input()

message = client.message.create(
        body= url,
         from_='+14157612923',
         to=to
)

print(message.sid)