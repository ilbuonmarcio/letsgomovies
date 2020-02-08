from selenium import webdriver
from bs4 import BeautifulSoup


class Film:
    def __init__(self, title, genres, link, trailer):
        self.title = title
        self.genres = genres
        self.link = link
        self.trailer = trailer

    def render(self):
        return f"""- ([TRAILER]({self.trailer})) [{", ".join(self.genres)}] [{self.title}]({self.link})"""


class TheSpaceWebParser():
    def __init__(self):
        pass

    def get_movies(self):
        driver = webdriver.Firefox()
        driver.get("https://www.thespacecinema.it/al-cinema")

        film_elements = driver.find_elements_by_class_name("filmlist__inner")

        films = []
        for elem in film_elements:
            elem_html = elem.get_attribute('innerHTML')
            soup = BeautifulSoup(elem_html, "html.parser")

            title = soup.find("a", {"class": "filmlist__title"})['data-adobe-title']
            link = "https://www.thespacecinema.it" + soup.find("a", {"class": "filmlist__title"})['href']
            trailer = soup.find("a", {"class": "filmlist__showfilm"})['data-videourl']
            genres = [genre.text for genre in soup.findAll("a", {"rv-href": "genre.url"})]

            films.append(Film(title, genres, link, trailer))

        driver.close()

        return films


if __name__ == "__main__":
    parser = TheSpaceWebParser()
    parser.get_movies()
