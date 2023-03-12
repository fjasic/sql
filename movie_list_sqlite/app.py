import datetime
import database

menu = """Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Watch a movie
5) View watched movies.
6) Exit.

Your selection: """
welcome = "Welcome to the watchlist app!"


print(welcome)
database.create_tables()


def prompt_add_new_movie():
    title = input("Add new movie title. ")
    release_date = input("Add new movie release date (dd-mm-YYYY). ")
    parsed_timestamp = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    release_timestamp = parsed_timestamp.timestamp()
    database.add_movies(title, release_timestamp)


def print_movies(heading, movies):
    print(f"---{heading} movies.---")
    for movie in movies:
        movie_date = datetime.datetime.fromtimestamp(movie[1])
        date = movie_date.strftime("%d %b %Y")
        print(f"{movie[0]} (on {date})")
    print("---\n")

while (user_input := input(menu)) != "6":
    if user_input == "1":
        prompt_add_new_movie()
    elif user_input == "2":
        movies = database.get_movies(upcoming=True)
        print_movies("upcoming", movies)
    elif user_input == "3":
        movies = database.get_movies()
        print_movies("all", movies)
    elif user_input == "4":
        movie_title = input("Enter movie title you have watched: ")
        database.watch_movie(movie_title)
    elif user_input == "5":
        movies = database.get_watched_movies()
        print_movies("watched", movies)
    else:
        print("Invalid input, please try again!")
