import json
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from database import Database

app = Flask(__name__)
app.secret_key = '7asj^4xVH755q'

db = Database()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    for field in data:
        if field['name'] == 'username':
            username = field['value']
        if field['name'] == 'password':
            password = field['value']
    user = db.login(username, password)
    if user is not None :
        session['loggedin'] = True
        session['username'] = user['username']
        resp = jsonify(success=True)
    else :
        resp = jsonify(success=False)
    return resp

@app.route('/profile', methods=['GET'])
def profile():
    if 'loggedin' in session:
        users = db.get_users_by_admin(session['username'])
        return render_template('profile.html', users= users, username=session['username'])
    else:
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('index'))

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    for field in data:
        if field['name'] == 'search':
            username = field['value']
        if field['name'] == 'managed_by':
            managed_by = field['value']
    user = db.get_users_by_admin(managed_by, username)
    if user is not None :
        resp = jsonify(user)
    else :
        resp = jsonify(success=False)
    return resp
