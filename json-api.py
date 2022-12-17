import json
import requests
import sqlite3
from random import randint

# Connect to the database
conn = sqlite3.connect('api_requests.db')

# Create a table to store API request data
conn.execute('''CREATE TABLE IF NOT EXISTS api_requests (id INTEGER PRIMARY KEY, food_choice TEXT, name TEXT, tagline TEXT, abv REAL)''')

food_choice = input('Please enter your dinner choice: ')

# Store the food choice in the database
conn.execute('''INSERT INTO api_requests (food_choice) VALUES (?)''', (food_choice,))

url = f'https://api.punkapi.com/v2/beers?food={food_choice}'

r = requests.get(url)

data = json.loads(r.text)

beer_list = []

for beer in data:
    name = beer['name']
    tagline = beer['tagline']
<<<<<<<<< Temporary merge branch 1
    

    beer_item = {
        'name': name,
        'tagline': tagline
    }
    beer_list.append(beer_item)
    
value = randint(0, len(beer_list))

try_this = beer_list[value]

try_name = try_this['name']
try_tagline = try_this['tagline']

print(f'You shuld try {try_name}, {try_tagline}')
=========
    alcohol = beer['abv']
    
>>>>>>>>> Temporary merge branch 2

    beer_item = {
        'name': name,
        'tagline': tagline,
        'abv': alcohol
    }
    beer_list.append(beer_item)

value = randint(0, len(beer_list))

try_this = beer_list[value]

try_name = try_this['name']
try_tagline = try_this['tagline']
try_abv = try_this['abv']

# Store the selected beer data in the database
conn.execute('''INSERT INTO api_requests (name, tagline, abv) VALUES (?, ?, ?)''', (try_name, try_tagline, try_abv))

# Commit the changes to the database
conn.commit()

print(f'You shuld try {try_name}, {try_tagline}, {try_abv}')

# Close the connection to the database
conn.close()
