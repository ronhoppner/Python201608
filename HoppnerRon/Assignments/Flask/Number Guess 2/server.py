# NUMBER GAME SERVER

from flask import Flask, session, render_template, url_for, request, redirect
app = Flask(__name__)
app.secret_key = '123456abcdefgh'

import random

@app.route('/')
def index():

	session['number'] = random.randrange(0, 101)
	return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():

	guess = int(request.form['guess'])

	if guess > session['number']:
		session['message'] = 'Too high.'
	elif guess < session['number']:
		session['message'] = 'Too low.'
	elif guess == session['number']:
		session['message'] = 'Nailed it!'
	return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():

	session['message'] = 0
	session.pop('number')
	return redirect('/')

app.run(debug=True)