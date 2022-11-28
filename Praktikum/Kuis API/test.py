import requests


response = requests.get('http://api.open-notify.org/astros.json')

#print(response.status_code)
print(response.json())
# jprint(response.json())
# results = response.json()['people']
# for people in results:
#     print(f"Nama: {people['name']}")
#     print(f"Lokasi: {people['craft']}\n")