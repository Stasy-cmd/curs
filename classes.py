import re
from abc import abstractmethod
from abc import ABC
import requests

class Engine(ABC):
    @abstractmethod
    def get_request(self):
        pass


class HH(Engine):
    def __init__(self, name, experience):
        self.name = name
        self.url = 'https://api.hh.ru/vacancies'
        self.experience = f'lessThan{experience}'

    def get_request(self, i):
        # параметры, которые будут добавлены к запросу
        par = {'text': 'python', 'experience.name': self.experience, 'area': '113', 'per_page': '10', 'page': i}
        return requests.get(self.url, params=par)


class Superjob(Engine):
    def __init__(self, name):
        self.name = name
        self.url = 'russia.superjob.ru'

    def get_request(self, i):
        url = f'vacancy/{self.url}/search/?keywords={self.name}&client_id=2041&client_secret=v3.r.137010722.c814f177a2a75780d1c3b3eee6c2078fc06d4e75.d884c121827c4507a37f3929e8b36dc3dc48a890&page={i}'
        print(url)
        #return request

class Vacancy:
    def __init__(self):
        self.name = None
        self.salary = None
        self.description = None
        self.url = None

    def __repr__(self):
        return f'{self.name}, {self.description}, {self.url}, {self.salary} '

    def set_name(self, name):
        name = re.sub('<span.*\">', '', name)
        self.name = re.sub('</span>', '', name)

    def set_description(self, name):
        name = re.sub('<span.*\">', '', name)
        self.description = re.sub('</span>', '', name)

    def set_url(self, url_1, url_2 = None):
        self.url = url_1 + url_2

