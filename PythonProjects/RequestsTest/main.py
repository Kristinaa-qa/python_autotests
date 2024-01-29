import requests

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json', 'trainer_token': '0feb7f2558864118d27008ae75fd7d0f'}

# body = {
#    "name": "Солнце",
#    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
# }

#response = requests.post(url=f'{URL}/pokemons', json=body, headers=HEADER)
#print(f'"Статус код: {response.status_code}. Сообщение: {response.text}')

# body = {
#    "pokemon_id": "28704",
#    "name": "Луна",
#    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
# }


# response = requests.put(url=f'{URL}/pokemons', json=body, headers=HEADER)
# print(f'"Статус код: {response.status_code}. Сообщение: {response.text}')

body = {
    "pokemon_id": "28704"
}

response = requests.post(url=f'{URL}/trainers/add_pokeball', json=body, headers=HEADER)
print(f'"Статус код: {response.status_code}. Сообщение: {response.text}')