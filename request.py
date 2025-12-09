import requests
import pprint

url = "https://api.hh.ru/vacancies"

name = input("Введите название вакансии: ")
city = input("Введите город: ")

params = {
    'text': 'NAME:name',
    # страница
    'page': 4
}

result = requests.get(url, params=params).json()

pprint.pprint(result)
# print(result['items'][0]['url'])
# print(result['items'][0]['alternate_url'])
