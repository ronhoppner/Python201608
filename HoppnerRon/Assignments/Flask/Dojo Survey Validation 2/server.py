from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'barstoolPigeons'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/result')
def result():
	return render_template('/result.html')

@app.route('/validate', methods=['POST'])
def validate():

	if len(request.form['name']) < 1:
		flash("Name field cannot be blank.")
		return redirect('/')
	elif len(request.form['comment']) > 121:
		flash("Comments cannot be more than 120 characters.")
		return redirect('/')
	else:
		session['name'] = request.form['name']
		session['location'] = request.form['location']
		session['language'] = request.form['language']
		session['comment'] = request.form['comment']
		return redirect('/result')
	
app.run(debug=True)