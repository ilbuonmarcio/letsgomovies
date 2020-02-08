import requests
from bs4 import BeautifulSoup


class Film:
    def __init__(self, title, poster, genres, link, trailer):
        self.title = title
        self.poster = poster
        self.genres = genres
        self.link = link
        self.trailer = trailer

    def render(self):
        return f"""- ([TRAILER]({self.trailer})) [{", ".join(self.genres)}] [{self.title}]({self.link})"""


class TheSpaceWebParser():
    def __init__(self):
        pass

    def get_movies(self):
        page = requests.get("https://www.thespacecinema.it/al-cinema")

        if page.status_code != 200:
            raise Exception("Unable to get movies")

        soup = BeautifulSoup(page.text, "html.parser")

        film_elements = soup.findAll("div", {"class": "ml-movie-boxes__figure"})
        
        films = []
        for elem in film_elements:
            film_title = elem.findChildren("img", {"class": "ml-movie-boxes__poster"})[0]['alt'].title()
            film_poster = elem.findChildren("img", {"class": "ml-movie-boxes__poster"})[0]['src']
            film_link = "https://www.thespacecinema.it" + elem.findChildren("a", {"class": "ml-movie-boxes__layer__link"})[0]['href']
            film_trailer = elem.findChildren("a", {"class": "ml-movie-boxes__layer__popup"})[0]['href']

            film_genres = []
            metadata = elem.findChildren("a", {"class": "ml-movie-boxes__layer__popup"})[0]['data-targeting']
            if "genre:" in metadata:
                for token in metadata.split("|"):
                    if "genre:" in token:
                        genres = token.replace("genre:", "").split(",")
                        for genre in genres:
                            film_genres.append(genre)

            films.append(
                Film(film_title, film_poster, film_genres, film_link, film_trailer))

        return films


if __name__ == "__main__":
    parser = TheSpaceWebParser()
    print(parser.get_movies())
