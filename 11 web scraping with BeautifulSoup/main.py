# pip install beautifulsoup4

from bs4 import BeautifulSoup
import requests


def scrap(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
    r = requests.get(url, headers=headers)
    c = r.content
    bs = BeautifulSoup(c, 'html.parser')
    cities = bs.find_all('div', {'class': 'cities'})
    for city in cities:
        name = city.find('h2').text
        desc = city.find('p').text
        print(name, '\t:', desc)


scrap('http://pyclass.com/example.html')
