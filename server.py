from flask import Flask, render_template, request, jsonify, Response, session, flash
from flask_cors import CORS
from config import Config
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from keyring import get_keyring, set_keyring
import os

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('overview.html')


@app.route('/login', methods=['POST'])
def login():
    user = os.environ.get('USERCRED')
    password = os.environ.get('PASSCRED')
    if request.form['psw'] == password and request.form['uname'] == user:
        session['logged_in'] = True
    else:
        flash('Wrong password!')
    return home()


@app.route('/overview')
def overview():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('overview.html')


@app.route('/contact')
def contact():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('contact.html')


@app.route('/about')
def about():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('about.html')


@app.route('/faq')
def faq():
    return render_template('faq.html')


@app.route('/newuser')
def newuser():
    return render_template('faq.html')


if __name__ == '__main__':
    app.secret_key = 'the most secret of keys'
    print(datetime.utcnow())
    app.run(host='0.0.0.0', port=6789, debug=True)
