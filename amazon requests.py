import requests
from bs4 import BeautifulSoup

HEADERS = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
URL = 'https://www.amazon.com/Official-Creality-Certified-Meanwell-220x220x250mm/dp/B07VMG98ZN/ref=sr_1_4?dchild=1&keywords=creality+ender+5pro&qid=1588543523&sr=8-4'
stock = 20


page = requests.get(URL, headers = HEADERS)
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.find_all(id='titleSection')
print(title)


