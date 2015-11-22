from twilio.rest import TwilioRestClient 
from secrets import TWILIO_SID
from secrets import TWILIO_AUTH
import serial

def addNumber(num):
    listNums.append(num)
 
ACCOUNT_SID = TWILIO_SID 
AUTH_TOKEN = TWILIO_AUTH
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

def sendAlert(_to, _from, _body):
    client.messages.create(
        to=_to,
        from_=_from,
        body=_body,
    )

ser = serial.Serial('/dev/cu.usbmodem1421', 115200)

while ser.read() == '1':
    ser.read()

print "ding dong"
ser.close()
