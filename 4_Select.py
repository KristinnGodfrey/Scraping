import requests 
from bs4 import BeautifulSoup
# Make a request
page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')

# select all h1 tags
all_h1_tags = []
for element in soup.select('h1'):
    all_h1_tags.append(element.text)

#select seventh p text
seventh_p_text = soup.select('p')[6].text

print(all_h1_tags, seventh_p_text)