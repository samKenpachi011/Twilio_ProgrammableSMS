from twilio.rest import Client
# Your Account Sid and Auth Token from twilio.com/console
account_sid = '###########################'
auth_token = '#############################'
mynumber='###########################'

client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="This is your message body",
                     from_='Your Registered Twilio Number',
                     to= mynumber
                 )

print(message.sid)