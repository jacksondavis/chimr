from flask import Flask, flash, jsonify, render_template, redirect, request
from flask_bootstrap import Bootstrap
import engine
from engine import client
import twilio.twiml
import serial
from twilio.rest import TwilioRestClient 

from secrets import TWILIO_SID
from secrets import TWILIO_AUTH
from secrets import SERIAL_PORT

ACCOUNT_SID = TWILIO_SID 
AUTH_TOKEN = TWILIO_AUTH
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

app = Flask(__name__)

ser = serial.Serial(SERIAL_PORT, 115200)

# Home Page
@app.route('/', methods=['GET', 'POST'])
def index():
	text = request.form.get('Body')
	if text is None:
		print(text)
		return render_template('index.html')

	else:
		print type(text)
		print type(str(text))
	  	ser.flushInput()
	  	print str(text)
	  	ser.write(str(text))
	  	return render_template('index.html')

@app.route("/test", methods=['GET', 'POST'])
def test():
	resp = twilio.twiml.Response()
	resp.message("Hello, Mobile Monkey")
	text = request.form.get('Body')

	print(str(text))
	print type(text)
	return 'hi'

if __name__ == "__main__":
	engine.buttonCheck(ser)
	app.run()
