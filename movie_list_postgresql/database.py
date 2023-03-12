import datetime
import psycopg2
import os

from dotenv import load_dotenv

load_dotenv()

connection = psycopg2.connect(os.environ["URL"])

# title, release_date, watched
CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies (
    title TEXT, release_timestamp REAL, watched INTEGER);"""

INSERT_MOVIES = (
    "INSERT INTO movies (title, release_timestamp, watched) VALUES (%s, %s, 0);"
)

SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp > %s;"
SELECT_WATCHED_MOVIES = "SELECT * FROM movies WHERE watched = 1;"
CHANGE_WATCHED_MOVIE = "UPDATE movies SET watched = 1 WHERE title = %s;"


def create_tables():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_MOVIES_TABLE)


def add_movies(title, release_timestamp):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_MOVIES, (title, release_timestamp))


def get_movies(upcoming=False):
    with connection:
        with connection.cursor() as cursor:
            if not upcoming:
                cursor.execute(SELECT_ALL_MOVIES)
            else:
                cursor.execute(
                    SELECT_UPCOMING_MOVIES, (datetime.datetime.today().timestamp(),)
                )
            return cursor.fetchall()


def watch_movie(title):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CHANGE_WATCHED_MOVIE, (title,))


def get_watched_movies():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_WATCHED_MOVIES)
            return cursor.fetchall()
