import os
import requests

headers = {'Authorization': 'Token %s' % os.environ['GITHUB_TOKEN']}
url='https://api.github.com/repos/andrewp-as-is/accepts.py/releases'
r = requests.get(url,headers=headers)
print(r)
print(r.json())
print(r.text)

url='https://api.github.com/repos/andrewp-as-is/accepts.py/releases/2020.4.1'
r = requests.delete(url,headers=headers)
