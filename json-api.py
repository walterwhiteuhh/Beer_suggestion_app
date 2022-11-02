import json
import requests

url = 'https://api.punkapi.com/v2/beers?food=pie'

r = requests.get(url)

data = json.loads(r.text)

#print(data[0]['name'], data[0]['tagline'], data[0]['abv'])

print(len(data))



