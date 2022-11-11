import requests

response = requests.get('https://api.spotify.com/')

print(response.status_code)