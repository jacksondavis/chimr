from flask import Flask, flash, jsonify, render_template, redirect
from flask_bootstrap import Bootstrap
import engine
from engine import client

app = Flask(__name__)

# Home Page
@app.route('/home')
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/message", methods=['GET', 'POST'])
def getText():
	engine.sendText()
    print(request.form['Body'])
    resp = twilio.twiml.Response()
    resp.message("Hello, Mobile Monkey")
    return str(resp)

@app.route('/test')
def testSend():
	engine.sendAlert()
	return render_template('index.html')

if __name__ == "__main__":
    app.run()