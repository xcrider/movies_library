library = []


class Movie:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre

        # VARIABLES

        self.counter = 0

    def __str__(self):
        return f"{self.title} ({self.year})" #Pulp Fiction (1994)

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
        return f"{self.title} S{self.season:02d}E{self.episode:02d}" #The Simpsons S01E05

    def _repr__(self):
        return f"Serires {self.title}, {self.year}, {self.genre}, {self.counter}"


def new_movie():

    title = input("Movie title: ")
    year = input("Year: ")
    genre = input("Genre: ")
    new_movie = Movie(title, year, genre)
    library.append(new_movie)


def new_series():

    title = input("Movie title: ")
    year = input("Year: ")
    genre = input("Genre: ")
    season = int(input("Season: "))
    episode = int(input("Episode: "))
    new_series = Series(title, year, genre, season, episode)
    library.append(new_series)


if __name__ == "__main__":

    series = Series(episode=1, season=1, title = "Lupin", year = 1982, genre="Action")
    movie = Movie(title = "Pulp Fiction", year= 1994, genre="Action")
