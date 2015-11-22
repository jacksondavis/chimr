from flask import Flask, flash, jsonify, render_template, redirect, request
from flask_bootstrap import Bootstrap
import engine
from engine import client
import twilio.twiml


from secrets import TWILIO_SID
from secrets import TWILIO_AUTH

from twilio.rest import TwilioRestClient 

ACCOUNT_SID = TWILIO_SID 
AUTH_TOKEN = TWILIO_AUTH
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

app = Flask(__name__)

# Home Page
@app.route('/home')
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/message", methods=['GET', 'POST'])
def getText():
	engine.sendText()
	return render_template('index.html')

@app.route("/test", methods=['GET', 'POST'])
def test():
	for i in range(0, 10):
		print i
	print(request.form.get('Body'))
	resp = twilio.twiml.Response()
	resp.message("Hello, Mobile Monkey")
	return str(resp)

if __name__ == "__main__":
	app.run(debug=True)