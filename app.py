from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return 'successful login <a href="/logout">Logout</a>'

@app.route('/login', methods=['POST'])
def do_admin_login():
    index = 0
    words = {'real'} #hardcoded password
    if request.form['username'] != 'user' or request.form['password'] not in words:
        return home()
    else:
        session['logged_in'] = True
    return home()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=4000)