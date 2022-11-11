import requests
from jprint import *

headers = {
    'apikey': 'c637ee50-6191-11ed-bb9c-dda00dac018f',
}

params = {
    'continent': 'Asia',
}

response = requests.get('https://app.sportdataapi.com/api/v1/soccer/countries', params=params, headers=headers)

# print(response.status_code)

# jprint(response.json())

results = response.json()['data']

for id in results:
    print("Country ID: " + str(results[id]['country_id']))
    print("Negara: " + results[id]['name'])
    print("Benua: " + results[id]['continent'])
    print()