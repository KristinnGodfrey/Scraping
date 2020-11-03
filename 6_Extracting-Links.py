import requests
from bs4 import BeautifulSoup
# Make a request
page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')

# Create top_items as empty list
all_links = []

for elem in soup.select('a'):
    text = elem.text
    text = text.strip() if text is not None else ''
    href = elem.get('href')
    href = href.strip() if text is not None else ''
    all_links.append({"href": href, "text": text})

print(all_links)

#to learn more about ternary if expressions: https://realpython.com/python-conditional-statements/