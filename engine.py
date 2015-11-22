from twilio.rest import TwilioRestClient 
from secrets import TWILIO_SID
from secrets import TWILIO_AUTH
from secrets import PHONE_NUMBER
import serial
 
ACCOUNT_SID = TWILIO_SID 
AUTH_TOKEN = TWILIO_AUTH
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

def sendAlert(_to, _from, _body):
    client.messages.create(
        to=_to,
        from_=_from,
        body=_body,
    )

def buttonCheck(ser):
    while ser.read() == '1':
        ser.read()

    sendAlert(PHONE_NUMBER, "+16305280456", "Ding Dong")
    print "ding dong"

