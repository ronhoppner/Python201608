from flask import Flask, session, render_template, url_for, request, redirect
app = Flask(__name__)
app.secret_key = '123456abcdef'

@app.route('/')
def index():
	try:
		session['count']
	except:
		session['count'] = 1
	session['count'] += 1

	return render_template('index.html')

@app.route('/reset', methods=['POST'])
def reset():
	session['count'] = 0
	return redirect('/')

app.run(debug=True)