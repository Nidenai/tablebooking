from urllib import request

from flask import Flask, render_template, redirect, url_for, session, request

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html', content='This is the content of the home page')
    else:
        return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/auth', methods=['POST'])
def auth():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'admin':
        session['username'] = username
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))