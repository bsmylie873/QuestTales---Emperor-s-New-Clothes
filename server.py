from flask import Flask, render_template, request, redirect, jsonify, Response, session, flash
from flask_cors import CORS
from qtdb_setup import init_db, db_session
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


@app.route('/login', methods=['GET', 'POST'])
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
        search = UserSearchForm(request.form)
        if request.method == 'POST':
            return search_results(search)

        return render_template('overview.html', form=search)


@app.route('/results', methods=['POST'])
def search_results(search):
    results = []
    search_string = search.data['search']

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


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('contact.html')


@app.route('/about', methods=['GET', 'POST'])
def about():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('about.html')


@app.route('/faq', methods=['GET', 'POST'])
def faq():
    return render_template('faq.html')


# @app.route('/newuser', methods=['GET', 'POST'])
# def new_user():
#     # form = UserForm(request.form)
#     # #return render_template('newuser.html', form=form)


if __name__ == '__main__':
    print(datetime.utcnow())
    app.run(host='127.0.0.1', port=6789, debug=True)
