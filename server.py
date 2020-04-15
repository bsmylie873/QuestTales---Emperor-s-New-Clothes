from flask import Flask, render_template, request, redirect, jsonify, Response, session, flash
from flask_wtf import Form
from flask_cors import CORS
from qtdb_setup import init_db, db_session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from model import User, Event, EventType
from form import UserSearchForm
from tables import UserResults
from app import app
import os

init_db()

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


@app.route('/overview', methods=['GET', 'POST'])
def overview():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        Search = UserSearchForm(request.form)
        if request.method == 'POST':
            return search_results

        return render_template('overview.html', form=Search)


@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['Search']

    if search_string == '':
        qry = app.query(User)
        results = qry.all()

    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        table = UserResults(results)
        table.border = True
        return render_template('results.html', table=table)


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


# @app.route('/newuser', methods=['GET', 'POST'])
# def new_user():
#     # form = UserForm(request.form)
#     # #return render_template('newuser.html', form=form)


if __name__ == '__main__':
    print(datetime.utcnow())
    app.run(host='0.0.0.0', port=6789, debug=True)
