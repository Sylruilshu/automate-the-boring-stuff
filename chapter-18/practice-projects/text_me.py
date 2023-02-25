from twilio.rest import Client


account_SID = "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
auth_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
twilio_number = "+xxxxxxxxxxx"
mobile_number = "+xxxxxxxxxxx"


def text_myself(message):
    twilio_client = Client(account_SID, auth_token)
    twilio_client.messages.create(body=message, from_=twilio_number, to=mobile_number)
