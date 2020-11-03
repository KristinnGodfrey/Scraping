import requests 
from bs4 import BeautifulSoup

page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/"
)
soup = BeautifulSoup(page.content, 'html.parser')

top_items = []
for elem in soup.select('div.thumbnail'):
    title = elem.select('h4 > a.title')[0].text
    rating = elem.select('div.ratings')[0].text
    info = {
        "title": title.strip(),
        "rating": rating.strip()
    }

    top_items.append(info)

print(top_items) 