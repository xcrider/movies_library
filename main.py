class Movie:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre

        # VARIABLES

        self.counter = 0


class Series(Movie):
    def __init__(self, episode, season):
        self.episode = episode
        self.season = season
