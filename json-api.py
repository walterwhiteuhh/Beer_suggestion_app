import json
import requests

url = 'https://api.punkapi.com/v2/beers'

r = requests.get(url)

data = json.loads(r.text)

