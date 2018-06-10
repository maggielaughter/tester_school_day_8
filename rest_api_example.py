import hashlib
import requests

BASE_URL='http://polakow.eu:3000/people/'


response = requests.get(BASE_URL, params={'_limit':3, '_page':2})
#print(response.json())
#print('**********')
#print(response.text)
#print(response.headers)
#print(response.status_code)
#print('************************************')
#print(response.headers['X-Total-count'])
#print('********************************************')
md5 = hashlib.md5('relayr'.encode('ascii'))
token = md5.hexdigest()
#print(token)
headers={'Authorization': 'Bearer ' + token}
person = {'first_name': 'Janusz', 'last_name': 'Cebularz',
          'email': 'janusz.cebularz@gmail.com',
          'phone': '+4851528587',
          'ip_address': '192.168.1.1'}
response = requests.post(BASE_URL, json=person, headers=headers)
#print(response.json())

url = BASE_URL + 'CfJJMuh'
#print(requests.get(url).json()) #pobranie konkretnego elementu
#print(requests.get(BASE_URL, params={'id': 'CfJJMuh'}).json()) #wyszukiwanie pasujących elementów

cebularze = requests.get(BASE_URL, params={'first_name': 'Michas','last_name': 'Cebularz'}).json()
#print(cebularze)

response= requests.get(BASE_URL, params={'email_like': '@gmail.com'})
print(response.json())

print('192.168.1.1'.startswith('192.168'))
print('abc'.startswith('123'))