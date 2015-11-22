from flask import Flask, flash, jsonify, render_template, redirect, request
from flask_bootstrap import Bootstrap
import engine
from engine import client
import twilio.twiml
import serial


from secrets import TWILIO_SID
from secrets import TWILIO_AUTH

from twilio.rest import TwilioRestClient 

ACCOUNT_SID = TWILIO_SID 
AUTH_TOKEN = TWILIO_AUTH
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

app = Flask(__name__)

ser = serial.Serial('/dev/cu.usbmodem1421', 115200)

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

<<<<<<< HEAD
@app.route("/", methods=['GET', 'POST'])
def getText():
    print "da fuq"
    #x = request.form.get('Body')
    x = raw_input("fuck bitches")
    ser = serial.Serial('/dev/cu.usbmodem1421', 115200)
    ser.write(x)
    ser.close()
    return render_template('index.html')
=======
#@app.route("/message", methods=['GET', 'POST'])
#def getText():
#	ser = serial.Serial('/dev/cu.usbmodem1421', 115200)
#	while ser.read() == '1':
#		ser.read()
#
#	print "ding dong"
#	text = request.form.get('Body')
#	while text == None:
#		text = request.form.get('Body')
#
#	print(text)
#	resp = twilio.twiml.Response()
#	resp.message("Hello, Mobile Monkey")
#	ser.write(text)
#	while ser.read() == '1':
#		ser.read()
#
#	sendAlert("+16307476759", "+16305280456", "Ding Dong")
#	ser.close()
#	return render_template('index.html')
>>>>>>> 725bd0c616c4c1e076a36311c7623157910babfb

@app.route("/test", methods=['GET', 'POST'])
def test():
	resp = twilio.twiml.Response()
	resp.message("Hello, Mobile Monkey")
	text = request.form.get('Body')

	print(str(text))
	print type(text)
	return 'hi'

#@app.route("/print", methods=['GET', 'POST'])
#def printThis():
#	ser = serial.Serial('/dev/cu.usbmodem1421', 115200)
#	while ser.read() == '1':
#		ser.read()
#
#	print "ding dong"
#	text = request.form.get('Body')
#
#	if text is None:
#		return
#
#	print(text)
#	resp = twilio.twiml.Response()
#	resp.message("Hello, Mobile Monkey")
#	ser.write(text)
#	while ser.read() == '1':
#		ser.read()
#
#	ser.close()
#	return render_template('index.html')

if __name__ == "__main__":
<<<<<<< HEAD
	app.run()
=======
	engine.buttonCheck(ser)
	app.run()
>>>>>>> 725bd0c616c4c1e076a36311c7623157910babfb
