"""CRUD operations"""

from model import db, User, Movie, Rating, connect_to_db
from datetime import datetime 


def create_user(email, password):
    """Create and return a new user."""

    user = User(email = email, password = password)

    db.session.add(user)
    db.session.commit()

    return user

def create_movie(title = None, overview = None, release_date = None, poster_path = None):
    """Create and return a new movie"""

    movie = Movie(title = title, 
                  overview = overview, 
                  release_date = release_date, 
                  poster_path = poster_path)

    db.session.add(movie)
    db.session.commit()

    return movie

def create_rating(user, movie, score):
    rating  = Rating(score = score, movie = movie, user = user)

    db.session.add(rating)
    db.session.commit()

    return rating

def get_movies():
    return db.session.query(Movie).all()

def get_movie_by_id(movie_id):
    return db.session.query(Movie).get(movie_id)

def get_users():
    return db.session.query(User).all()

def get_user_by_id(user_id):
    return db.session.query(User).get(user_id)


if __name__ == '__main__':
    from server import app
    connect_to_db(app)