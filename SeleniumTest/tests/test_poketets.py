import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2/'
TOKEN = '3811be9886ffabf56f488c1b1990278b'
HEADERS = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

def test_status_code_200():
    response = requests.get(url= f'{URL}trainers', params = {"trainer_id" : 141})
    assert response.status_code == 200

def test_name():
    response = requests.get(url= f'{URL}trainers', params = {"trainer_id" : 141})
    assert response.json()['data'][0]['trainer_name'] == 'Potato'

