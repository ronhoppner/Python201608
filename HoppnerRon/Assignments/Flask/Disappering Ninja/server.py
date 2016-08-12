from flask import Flask, render_template, request
app = Flask(__name__)


turtles = {
		'red':'raphael.jpg',
		'blue':'leonardo.jpg',
		'purple':'donatello.jpg',
		'orange':'michelangelo.jpg',
		'april':'notapril.jpg'
		}

@app.route('/ninja')
def index():
	return render_template('index.html', turtles = turtles)

@app.route('/ninja/<color>')
def show(color):
	data = {}
	if color == 'red' or color == 'blue' or color == 'purple' or color == 'orange':
		data[color] = turtles[color]
	else:
		data['april'] = turtles['april']
	return render_template('index.html', turtles = data)



app.run(debug=True)

