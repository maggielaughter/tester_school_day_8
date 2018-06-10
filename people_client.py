import requests
"""kod do poprawy"""
class PeopleClient:

    def __init__(self, base_url):
        self.base_url = base_url


    def get_all(self, limit):
        if limit == None:
            return requests.get(self.base_url).json()
        elif limit >0:
            response = requests.get(self.base_url, params={'_page':limit})
            people = response.json()
            page_number = int(response.headers['X-Total-count'])

            if page_number % limit == 0:
                page = page_number // limit
            else:
                page = page_number // limit + 1

            for page in range(2, page + 1):
                chunk=requests.get(self.base_url, params={'_limit': limit, '_page': page}).json()
                
                people.extend(chunk)
                
            return people

    def quer(self, **criteria):
        

if __name__ == '__main__':
    client = PeopleClient('http://polakow.eu:3000/people/')
    print(client.get_all(250))


people=client.get_all(None)
people2 = client.get_all(200)

print(people == people2)

