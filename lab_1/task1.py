import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime, date

practice_date = date(2019, 9, 24)


def get_html_page(url):
    news_request = requests.get(url)
    if news_request.status_code == 200:
        return news_request.text
    else:
        print('Oops! Something went wrong...')
        return 0

def find_articles(html_page):
    parsed_page = BeautifulSoup(html_page, features='html.parser')
    headers = []
    for t in parsed_page.findAll('h4'):
        headers.append(t.string)
    return headers


headers = find_articles(get_html_page('https://sobesednik.ru/psychology'))

articles = [{'title': i} for i in headers]


def publish_report(path, articles):
    artjson = {'url': 'https://sobesednik.ru/psychology', 'creation Date': '{0}'.format(practice_date),
               'articles': articles}
    with open(path, "w") as write_file:
        json.dump(artjson, write_file)
    return artjson


publish_report('data_file.json', articles)

with open("data_file.json", "r") as read_file:
    data = json.load(read_file)

print(data)
