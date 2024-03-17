import requests

URL = 'https://api.pokemonbattle.me/v2/'
TOKEN = '3811be9886ffabf56f488c1b1990278b'
HEADERS = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": 'generate',
    "photo": 'generate'
}
body_put = { 
    "pokemon_id": "14231",
    "name": 'generate',
    "photo": 'generate'
}
body_ball = {"pokemon_id": "14231"}

response = requests.post(url = f'{URL}pokemons', headers = HEADERS, json = body_create)
print(response.text)

response_put = requests.put(url = f'{URL}pokemons', headers = HEADERS, json = body_put)
print(response_put.text)

response_ball = requests.post(url = f'{URL}trainers/add_pokeball', headers = HEADERS, json = body_ball)
print(response_ball.text)



