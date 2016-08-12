from flask import Flask, render_template, redirect, request, session, flash

import re #create a regular expression (RegEx)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():

  return render_template('index.html')

@app.route('/process', methods=['Post'])
def process():

	formData = {
		'email':request.form['email'],
		'fname':request.form['fname'],
		'lname':request.form['lname'],
		'password':request.form['password'],
		'confirmed':request.form['pwordconfirm']
		}

	if len(request.form['email']) < 1:
		flash("Email field cannot be blank.")
	elif not EMAIL_REGEX.match(request.form['email']):
		flash('Email address invalid.')
	elif len(request.form['fname']) < 1:
		flash("First name required.")
	elif request.form['fname'].isalpha() == False:
		flash('First name cannot contain numbers or special characters.')
	elif request.form['lname'].isalpha() == False:
		flash('Last name cannot contain numbers or special characters.')
	elif len(request.form['lname']) < 1:
		flash("Last name required.")
	elif len(request.form['password']) < 8:
		flash("Password too short. Password must be at least 8 characters.")
	elif request.form['password'].isalpha() == True:
		flash('Please include a number or special character in your password. For safety.')
	elif request.form['password'] != request.form['pwordconfirm']:
		flash('Password confirmation failed. Passwords do not match.')
	else:
		flash("Thank you for submitting!")
	print formData # Probably a bad idea to do this IRL, but useful for the learning process.
	return redirect('/')

app.run(debug=True)