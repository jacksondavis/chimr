from twilio.rest import TwilioRestClient 
from secrets import TWILIO_SID
from secrets import TWILIO_AUTH
import serial

listNums = []

def addNumber(num):
    listNums.append(num)
 
ACCOUNT_SID = TWILIO_SID 
AUTH_TOKEN = TWILIO_AUTH
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

#"+16304701481"
#"+16305280456"
#"Someone entered!"

def sendAlert(_to, _from, _body):
	client.messages.create(
	    to=_to, 
	    from_=_from, 
	    body=_body,  
	)

def sendText():
	connected = False

	ser = serial.Serial('/dev/cu.usbmodem1421', 9600)

	while not connected:
		serin = ser.read()
		connected = True

	ser.write("1")

	while ser.read() == '1':
		ser.read()
	sendAlert("+16307476759", "+16305280456", "Ding Dong")
	ser.close()
	print "closed"
