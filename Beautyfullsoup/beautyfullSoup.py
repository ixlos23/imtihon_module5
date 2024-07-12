import requests
import bs4


def beautyfullsoup(): # noqa
    html = requests.get('https://fitnessblender.com').content
    soup = bs4.BeautifulSoup(html, 'html.parser')
    return soup.find('div', {'class': 'vue cards'}).text