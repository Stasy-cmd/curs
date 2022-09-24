import re

import requests      # Для запросов по API
import json          # Для обработки полученных результатов
import time          # Для задержки между запросами
import os            # Для работы с файлами

from classes import HH, Superjob, Vacancy

vacancies = []
#цикл, который скачивает вакансии
# hh = HH('Python', '1')
# sj = Superjob('Python')
# for i in range(1, 100):
#     # запрос
#     sj.get_request ( i )
#     # vacancies.append(.json())

#print(vacancies)
a = requests.get('https://russia.superjob.ru/vacancy/search/?keywords=python').content.decode('utf-8')

r = a.split('f-test-search-result-item', maxsplit=1)[1]
k = r.split('f-test-search-result-item')
for i in k:
    #print(i)
    if 'href="' in i:
        temp = i.split('href="', maxsplit=1)[1]
        vacancies.append(temp.split('<br/></span></div><div class=')[0])
    #print(vacancies)
arr = []
for i in vacancies:
    if 'Разместите' not in i:
        v = Vacancy()
        temp = i.split('">', maxsplit=1)
        v.set_url('https://russia.superjob.ru/', temp[0])
        temp = temp[1].split('</a>', maxsplit=1 )
        v.set_name(temp[0])

        if 'По договорённости<' not in temp[1]:
            if '<!-- -->—<!-- --> ' in temp[1]:
                temp = re.split('<!-- -->—<!-- --> ', temp[1], maxsplit=1)[1]
            if '<!-- --> <!-- -->' in temp[1]:
                salary = re.split('<!-- --> <!-- -->', temp[1], maxsplit=1)[1].split('</span>', maxsplit=1)[0]
                v.salary = salary
                temp = re.split('</span.*">', temp[1], maxsplit=1)[1]
                v.set_description(temp)
        else:
            v.salary = 'По договорённости'
            temp = re.split('</span>.*\">', temp[1], maxsplit=1)
            v.set_description(temp[1])
        arr.append(v)
    # print(temp[0])
    # temp = re.split ('от', temp[1], maxsplit=1)
    # v.salary = temp[1]
    # arr.append(v)
    # print("")
# URL = 'https://api.superjob.ru/3.0/vacancies/?keywords%5B0%5D%5Bkeys%5D=&keywords%5B1%5D%5Bsrws%5D=1&keywords%5B1%5D%5Bskwc%5D=and&keywords%5B1%5D%5Bkeys%5D=php&keywords%5B2%5D%5Bsrws%5D=3&keywords%5B2%5D%5Bskwc%5D=particular&keywords%5B2%5D%5Bkeys%5D=javascript'
# a = requests.get('https://www.superjob.ru/vacancy/search/?keywords=python&geo%5Bt%5D%5B0%5D=4&page=2')
# for i in range(10):
#     a = requests.get(f'https://www.superjob.ru/vacancy/search/?keywords=python&geo%5Bt%5D%5B0%5D=4&page={i}')
# print(a)

for i in arr:
    print(i)