"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = 'dev'
app.jinja_env.undefine = StrictUndefined


# Replace this with routes and view functions!
@app.route('/')
def homepage():
    """Render root page of website"""

    return render_template('homepage.html')

@app.route('/movies')
def movies():
    """View all movies"""
    
    movies = crud.get_movies()

    return render_template('all_movies.html', movies = movies)


@app.route('/movies/<movie_id>')
def movie_detail(movie_id):
    
    movie = crud.get_movie_by_id(movie_id)

    return render_template('movie_details.html', movie = movie)

@app.route('/users')
def users():
    """View all users"""

    users = crud.get_users()

    return render_template('all_users.html', users = users)

@app.route('/users/<user_id>')
def user_detail(user_id):

    user = crud.get_user_by_id(user_id)

    return render_template('user_details.html', user = user)

@app.route('/users', methods = ['POST'])
def create_account():
    """Create a new user"""

    email = request.form.get('email')
    password = request.form.get('password')

    if crud.get_user_by_email(email):
        flash('That email is already assigned to a registered account.')

    else: 
        crud.create_user(email, password)
        flash('User successfully registered')
    
    return redirect('/')

@app.route('/log-in')
def log_in():
    email = request.args.get('email')
    password = request.args.get('password')

    if crud.get_password_by_email(email) == password: 
        flash('Logged In!')
        session['user_id'] = crud.get_user_id_by_email(email)
        print(session)
        return redirect('/')
    else:
        flash('Log-in Failed')
        return redirect('/')




if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
