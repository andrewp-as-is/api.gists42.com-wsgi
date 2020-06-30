import requests
import django
import os
import sys

headers = {'Authorization': 'Token a634a1134e0a6820ce0f41e953da5f22'}
files = {'requires42-files2.py':open('requires42-files.py','rb')}
url='http://127.0.0.1:8000/requires'
r = requests.post(url,headers=headers,files=files)
print(r)
print(r.text)
