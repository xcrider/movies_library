import random

library = []


class Movie:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre

        # VARIABLES

        self.counter = 0

    def __str__(self):
        return f"{self.title} ({self.year}) {self.counter}"

    def _repr__(self):
        return f"Movie {self.title}, {self.year}, {self.genre}, {self.counter}"

    def play(self):
        print(f"Playing {self.title}")
        self.counter += 1


class Series(Movie):

    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season = season
        self.episode = episode

    def __str__(self):
        return f"{self.title} S{self.season:02d}E{self.episode:02d} {self.counter}"

    def _repr__(self):
        return f"Series {self.title}, {self.year}, {self.genre}, {self.counter}"


def new_movie():

    title = input("Movie title: ")
    year = input("Year: ")
    genre = input("Genre: ")
    new_movie = Movie(title, year, genre)
    library.append(new_movie)
    print("New movie added!")


def new_series():

    title = input("Series title: ")
    year = input("Year: ")
    genre = input("Genre: ")
    season = input("Season: ")
    episode = input("Episode: ")
    new_series = Series(title, year, genre, season, episode)
    library.append(new_series)
    print("New series added!")


def get_library():

    for i, title in enumerate(library):
            print(f"{i}) {title}")


def get_movies():

    movies_libary = []
    for title in library:
        if isinstance(title, Series):
            continue
        else:
            movies_libary.append(title)

    movies_libary = sorted(movies_libary, key=lambda movie: movie.title)
    print("Movies in alphabetic order: ")
    for movie in movies_libary:
        print(movie)


def search(search_title):

    print("Searching…")
    for movie in library:
        if movie.title == search_title:
            print(f"Here it is: {movie}")
            break
    else:
        print("Oops… we don't have that one in library. Here's a full list of available titles: ")
        get_library()


def generate_views():

    print("Generating views for: ")
    x = random.choice(library)
    print(x)
    y = random.randint(1, 100)
    x.counter += y
    print(f"Added {y} in total of {x.counter} views")


def start_off(generator):

    for i in range(0, generator):

        generate_views()
        i += 1


def top_titles(top_items):

    top_list = sorted(library, key=lambda item: item.counter, reverse=True)

    print("Top list:")

    for i in range(0, top_items):
       print(top_list[i])


if __name__ == "__main__":

    print("Movies library")

    movie1 = Movie(title = "Gra", year=1990, genre = "Dramat")
    movie2 = Movie(title = "Zielona Mila", year= 1990, genre = "Dramat")
    movie3 = Movie(title = "Skazani na Showshank", year=1999, genre = "Dramat")

    series1 = Series(title = "Breaking Bad", year=2016, genre = "Dramat", episode=12, season=6)
    series2 = Series(title = "The Crown", year=2019, genre = "Dramat", episode=12, season=3)
    series3 = Series(title = "Lupin", year=2020, genre = "Dramat", episode=10, season=1)

    library = [movie1, series1, movie2, series2, movie3, series3]

    start_off(10)
    get_library()
    top_titles(3)
