from twilio.rest import TwilioRestClient 
from secrets import TWILIO_SID
from secrets import TWILIO_AUTH

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

sendAlert("+16304701481", "+16305280456", "Someone entered!")
