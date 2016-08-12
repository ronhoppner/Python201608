from flask import Flask, redirect, session, render_template, request
app = Flask(__name__)
app.secret_key = 'supersecretkeystuff'

import datetime
import random

@app.route('/')
def index():

	try:
		session['gold']
	except:
		session['gold'] = 0
	try:
		session['summary']
	except:
		session['summary'] = []


	return render_template('ninja_gold.html')

@app.route('/process_money', methods=['POST'])
def process():
	if request.form['action'] == 'farm':
		earn = random.randrange(10, 21)
		session['gold'] += earn
		session['summary'].append({'alert': 'Earned' + str(earn) + ' gold from the farm!' + datetime.datetime.now().strftime('%Y/%m/%d %I:%M %p' + '\n')})
	elif request.form['action'] == 'cave':
		earn = random.randrange(5, 11)
		session['gold'] += earn
		session['summary'].append({'alert': 'Earned' + str(earn) + ' gold from the cave!' + datetime.datetime.now().strftime('%Y/%m/%d %I:%M %p' + '\n')})
	elif request.form['action'] == 'house':
		earn = random.randrange(2, 6)
		session['gold'] += earn
		session['summary'].append({'alert': 'Earned' + str(earn) + ' gold from the house!' + datetime.datetime.now().strftime('%Y/%m/%d %I:%M %p' + '\n')})
	elif request.form['action'] == 'casino':
		earn = random.randrange(-50, 51)
		session['gold'] += earn
		session['summary'].append({'alert': 'Earned' + str(earn) + ' gold from the farm!' + datetime.datetime.now().strftime('%Y/%m/%d %I:%M %p' + '\n')})
	return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
	session.pop('gold')
	session.pop('summary')
	return redirect('/')

app.run(debug=True)

session['activities'].append({'color': 'green', 'alert': 'Earned ' + str(earn) + ' gold from the farm! ' + datetime.datetime.now().strftime('%Y/%m/%d %I:%M %p') + '\n'})