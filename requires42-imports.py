import requests

headers = {'Authorization': 'Token 06454b2f03c92c87119448838ec31b2716c21a70'}
data = dict(imports=['django','requests','sqlalchemy'])
url='https://api.requires42.com/requires'
r = requests.post(url,headers=headers,data=data)
print(r)
print(r.text)
