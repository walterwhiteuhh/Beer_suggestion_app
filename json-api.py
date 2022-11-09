import json
import requests

food_choice = input('Please enter your dinner choice: ')

url = f'https://api.punkapi.com/v2/beers?food={food_choice}'

r = requests.get(url)

data = json.loads(r.text)

print(data[0]['name'], data[0]['tagline'], data[0]['abv'])

#print(len(data))



