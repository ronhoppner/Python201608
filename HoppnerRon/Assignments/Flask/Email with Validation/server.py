from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector

import re #create a regular expression (RegEx)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
mysql = MySQLConnector(app, 'emailaddresses') #name of db you're working with goes here
app.secret_key = 'safetyThird'

@app.route('/')
def index():
	
	return render_template('index.html')

@app.route('/validate', methods = ['post'])
def create():

	print request.form['address']
	address = request.form['address']
	match = re.match(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', address)
	if match == None:
		flash('Invalid Email Address.')
	else:
		msg = "The email address you entered (" + address + ") is a VALID email address! Thank you!"
		flash('Valid email.')
		data = {'address':request.form['address']}
		query = "INSERT INTO email (address, created_at, updated_at) VALUES (:address, NOW(), NOW())"
		mysql.query_db(query, data) #query and data both written above
	return redirect('/result')


@app.route('/result')
def result():

	query = 'SELECT address, created_at FROM email'
	addresses = mysql.query_db(query)
	return render_template('result.html', all_addresses = addresses)
app.run(debug=True)

