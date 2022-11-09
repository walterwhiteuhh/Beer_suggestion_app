import json
import requests

food_choice = input('Please enter your dinner choice: ')

url = f'https://api.punkapi.com/v2/beers?food={food_choice}'

r = requests.get(url)

data = json.loads(r.text)

beer_list = []

for beer in data:
    name = beer['name']
    tagline = beer['tagline']
    

    beer_item = {
        'name': name,
        'tagline': tagline
    }
    beer_list.append(beer_item)




