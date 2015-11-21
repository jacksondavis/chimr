from twilio.rest import TwilioRestClient 
from secrets import TWILIO_SID
from secrets import TWILIO_AUTH

listNums = []

def addNumber(num):
    listNums.append(num)
 
ACCOUNT_SID = TWILIO_SID 
AUTH_TOKEN = TWILIO_AUTH
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

def sendAlert(): 
	client.messages.create(
	    to="+16304701481", 
	    from_="+16305280456", 
	    body="Someone entered!",  
	)
