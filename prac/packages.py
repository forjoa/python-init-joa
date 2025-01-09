import requests

response = requests.get('https://api.github.com/users/forjoa')

data = response.json()

if 'avatar_url' in data:
    print(data['avatar_url'])
else:
    print('No hay foto')