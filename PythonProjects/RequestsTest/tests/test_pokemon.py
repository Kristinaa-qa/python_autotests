import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json', 'trainer_token': '0feb7f2558864118d27008ae75fd7d0f'}

def test_get_trainers():
    """
    KTI-1. Get trainers status cod 200
    """
    response = requests.get(url=f'{URL}/trainers')
    assert response.status_code == 200, 'Unexpected status code'

def test_get_trainers_by_id():
    """
    KTI-2. Get trainers by id
    """
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id': 3703}, timeout=5)
    assert response.status_code == 200, 'Unexpected status code'
