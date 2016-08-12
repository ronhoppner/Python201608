from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = 'topsecret'

@app.route('/')
def index():
	return render_template('new.html')

@app.route('/result', methods=['POST'])
def result():
	data = request.form
	print data
	return render_template('result.html', data=data)

app.run(debug=True)