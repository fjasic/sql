import datetime
import sqlite3

connection = sqlite3.connect("database.db")
# title, release_date, watched
CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies (
    title TEXT, release_timestamp REAL, watched INTEGER);"""

INSERT_MOVIES = (
    "INSERT INTO movies (title, release_timestamp, watched) VALUES (?, ?, 0);"
)

SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp > ?;"
SELECT_WATCHED_MOVIES = "SELECT * FROM movies WHERE watched = 1;"
CHANGE_WATCHED_MOVIE = "UPDATE movies SET watched = 1 WHERE title = ?;"


def create_tables():
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)


def add_movies(title, release_timestamp):
    with connection:
        connection.execute(INSERT_MOVIES, (title, release_timestamp))


def get_movies(upcoming=False):
    with connection:
        if not upcoming:
            cursor = connection.execute(SELECT_ALL_MOVIES)
        else:
            cursor = connection.execute(
                SELECT_UPCOMING_MOVIES, (datetime.datetime.today().timestamp(),)
            )
        return cursor.fetchall()


def watch_movie(title):
    with connection:
        connection.execute(CHANGE_WATCHED_MOVIE, (title,))


def get_watched_movies():
    with connection:
        cursor = connection.execute(SELECT_WATCHED_MOVIES)
    return cursor.fetchall()
