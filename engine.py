from twilio.rest import TwilioRestClient 
 
ACCOUNT_SID = "its a secret huehuehue" 
AUTH_TOKEN = "what part of secret do you not understand" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
client.messages.create(
    to="+16304701481", 
    from_="+16305280456", 
    body="Someone entered!",  
)
