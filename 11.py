from bs4 import BeautifulSoup
from fake_user_agent import UserAgent
import requests

def parse():
    url = 'https://www.imdb.com/chart/top/'
    ua = UserAgent()
    rand_ua = ua.random
    headers = {'User-Agent': rand_ua}

    page = requests.get(url, headers=headers)
    Rang = {}

    if page.status_code == 200:
        soup = BeautifulSoup(page.text, "html.parser")
        films = soup.findAll('tr')

        for film in films:
            title_tag = film.find('td', class_='titleColumn')
            rating_tag = film.find('td', class_='ratingColumn imdbRating')

            if title_tag and rating_tag:
                name = title_tag.a.text.strip()
                rating = rating_tag.strong.text.strip()
                Rang[name] = rating 

        for name, rating in Rang.items():
            print(f"{name}: {rating}")

    else:
        print(page.status_code, " - ошибка подключения")

if __name__ == "__main__":
    parse()
