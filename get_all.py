import requests
import hashlib

class PeopleClientEroor(Exception):
    pass

class PeopleClient:

    RESPONSE_DICT = ('first_name', 'last_name', 'email', 'phone', 'ip_address')

    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token

    def get_all(self, limit=None):
        if limit is None:
            return requests.get(self.base_url).json()
        if limit <= 0:
            raise ValueError('Limit has to be positive.')

        response = requests.get(self.base_url, params={'_limit': limit})
        total_records = int(response.headers['X-Total-Count'])
        pages_count= total_records // limit
        if total_records % limit != 0:
            pages_count += 1
        people = response.json()
        for page in range(2, pages_count + 1):
            chunk=requests.get(self.base_url, params={'_limit': limit, '_page': page}).json()

            people.extend(chunk)
            #for person in chunk:
            #    people.append(person)
        return people

    def add_person(self, first_name, last_name, email, phone, ip_adress):
        headers = {'Authorization': 'Bearer ' + self.token}
        person = {'first_name': first_name,
                  'last_name': last_name,
                  'email': email,
                  'phone': phone,
                  'ip_address': ip_adress}
        response = requests.post(self.base_url, json=person, headers=headers)
        if response.status_code != 201: #if not respons.ok
            raise PeopleClientEroor(response.json()['error'])
        return response.json()

    def person_by_id(self, person_id):
        url = self.base_url + person_id
        response = requests.get(url)
        #response.raise_for_status()
        if response.status_code == 404:
            raise PeopleClientEroor('User with given id not found')
        elif not response.ok:
            raise PeopleClientEroor('Unknown error.')
        return response.json()

    def query(self, **criteria):
        for key in criteria:
            if key not in self.RESPONSE_DICT:
                raise ValueError('Unknown error' + key)
        return requests.get(self.base_url, params={**criteria})

    def people_by_partial_ip(self, partial_ip):
        ip_regexp = '^' + partial_ip
        return requests.get(self.base_url, params={'ip_addres_like': ip_regexp}).json()


if __name__ == '__main__':
    token = hashlib.md5('relayr'.encode('ascii')).hexdigest()
    client = PeopleClient('http://polakow.eu:3000/people/', token)


people=client.get_all()
people2 = client.get_all(200)
#print(client.add_person('Ada', 'Mazak', 'gosia.mazaki@nteria.pl', '+48662039104', '192.195.1.1'))
#print(people == people2)
people3 = client.person_by_id('CfJJMuh')
print(people3)

janusze = client.query(first_name='Janusz', last_name='Polak', ip_address='0.0.0.0').json()
print(janusze)

search_ip=client.people_by_partial_ip('192.168')
print(search_ip)