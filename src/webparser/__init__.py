import time
import requests
import itertools

from bs4 import BeautifulSoup
from pprint import pprint


class TheSpaceWebParser():
    def __init__(self):
        pass

    def get_movies(self):
        page = requests.get("https://www.thespacecinema.it")

        if page.status_code != 200:
            raise Exception("Unable to get movies")

        soup = BeautifulSoup(page.text, "html.parser")

        film_elements = soup.findAll("div", {"class": "ml-movie-boxes__figure"})
        
        films = []
        for elem in film_elements:
            film_title = elem.findChildren("img", {"class": "ml-movie-boxes__poster"})[0]['alt']
            film_poster = elem.findChildren("img", {"class": "ml-movie-boxes__poster"})[0]['src']
            film_link = "https://www.thespacecinema.it" + elem.findChildren("a", {"class": "ml-movie-boxes__layer__link"})[0]['href']
            film_trailer = elem.findChildren("a", {"class": "ml-movie-boxes__layer__popup"})[0]['href']

            film_genres = list(itertools.chain(*[token.replace("genre:", "").split(",") for token in elem.findChildren("a", {"class": "ml-movie-boxes__layer__popup"})[0]['data-targeting'].split('|') if "genre:" in token]))
            
            print(film_genres)



if __name__ == "__main__":
    parser = TheSpaceWebParser()
    parser.get_movies() 