from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def index():
    query = "SELECT * FROM friends"                           # define your query
    friends = mysql.query_db(query)                           # run query with query_db()
    return render_template('index.html', all_friends=friends) # pass data to our template

#CREATE A USER "C"

@app.route('/friends', methods=['POST'])
def create():
  
    query = "INSERT INTO friends (first_name, last_name, created_at, updated_at) VALUES (:first_name, :last_name, NOW(), NOW())" #Query written as a string

    data = {												#Create a dictionary of data from the POST data received.
        'first_name': request.form['first_name'], 
        'last_name':  request.form['last_name']
    }
    mysql.query_db(query, data)								# Run query, with dictionary values injected into the query.
    return redirect('/')

#READ A SPECIFIC USER "R"

@app.route('/friends/<id>')
def show(id):

    data = {'single_friend': id}											
    
    query = 'SELECT id, first_name, last_name, created_at FROM friends WHERE id = :single_friend'
    friend = mysql.query_db(query, data)
    return render_template('index.html', all_friends=friend)

#UPDATE A USER "U"

@app.route('/update_friend/<id>', methods=['POST'])
def edit(id):
    
    data = {'id': id}

    query = "SELECT first_name, last_name FROM friends WHERE id = :id"

    mysql.query_db(query, data)
    return render_template('update.html', friend=data)

@app.route('/save_update/<id>', methods=['POST'])
def save(id):

    data = {'id': id, 'first_name': request.form['first_name'], 'last_name': request.form['last_name']}

    query = 'UPDATE friends SET first_name=:first_name, last_name=:last_name, updated_at=NOW() WHERE id=:id'

    mysql.query_db(query, data)
    return redirect('/')
#DELETE A USER "D"

@app.route('/remove_friend/<friend_id>', methods=['POST'])

def delete(friend_id):
    query = "DELETE FROM friends WHERE id = :id"
    
    data = {'id': friend_id}

    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)