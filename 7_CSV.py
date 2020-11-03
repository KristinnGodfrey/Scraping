import requests
from bs4 import BeautifulSoup
import csv 

# Make a request
page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')

all_products = []

for elem in soup.select('div.thumbnail'):
    title = elem.select('h4 > a')[0].text.strip()
    description = elem.select('p.description')[0].text.strip()
    price = elem.select('h4.price')[0].text.strip()
    review = elem.select('div.ratings')[0].text.strip()    
    image = elem.select('img')[0].get('src')

    all_products.append({
        "name": title,
        "description": description,
        "price": price,
        "reviews": review,
        "image": image
    })

keys = all_products[0].keys()

with open('products.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(all_products)