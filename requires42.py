import requests


headers = {'Authorization': 'Token bbe8b0e63a8ed33fcd8d30789d2d461612bfe9e9'}
data = dict(imports=['requests','sqlalchemy'])
url='http://127.0.0.1:8000/requires'
r = requests.post(url,headers=headers,data=data)
print(r)
print(r.json())
