import requests
from pprint import pprint

pokemon_number = input("What is the pokemon's ID? ")

url = 'http://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)

response = requests.get(url)
#print(response)

pokemon = response.json()
#pprint(pokemon)

print('Name of the pokemon is:',pokemon['name'])
print('height of the pokemon is:',pokemon['height'])
print('weight of the pokemon is:',pokemon['weight'])

moves = pokemon['moves']
count = 0
for move in moves:
    print(move['move']['name'])
    count += 1
print(count)

print('next code')
url = 'https://pokeapi.co/api/v2/item/28/'
response = requests.get(url)
data = response.json()
print(data['name'])