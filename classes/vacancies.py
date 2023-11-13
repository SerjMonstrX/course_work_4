import json
import os
import requests
from abc import ABC, abstractmethod


class JobSitesAPI(ABC):

    @abstractmethod
    def get_requests(self):
        pass

    @abstractmethod
    def save_to_json(self, vacancies_data, filename):
        pass

    @abstractmethod
    def load_from_json(self, filename):
        pass


class HH_API(JobSitesAPI):
    def __init__(self, keyword, page=0):
        self.url = "https://api.hh.ru/vacancies"
        self.params = {
            "text": keyword,
            "page": page
        }
        self.filename = 'hh_data.json'  # Используем относительный путь

    def get_requests(self):
        ''' Функция для запроса данных с сайта HH по API'''

        try:
            response = requests.get(self.url, params=self.params)
            response.raise_for_status()  # Это вызовет исключение, если код состояния не 200

            try:
                vacancies_data = response.json().get('items', [])
            except json.JSONDecodeError as json_error:
                print(f"Ошибка декодирования JSON: {json_error}")
                vacancies_data = []

            return vacancies_data

        except requests.RequestException as e:
            print(f'Ошибка {response.status_code}: {response.text}')
            raise RuntimeError(f"Не удалось получить вакансии с HH: {str(e)}")

    def save_to_json(self, vacancies_data, filename=None):
        ''' Функция для сохранения данных в JSON файл'''

        if filename is not None:
            self.filename = filename
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump(vacancies_data, file, ensure_ascii=False, indent=2)
            print(f"Вакансии успешно сохранены в файл {self.filename}")
        except IOError as e:
            raise RuntimeError(f"Ошибка при записи вакансий в JSON: {str(e)}")

    def load_from_json(self, filename=None):
        ''' Функция для загрузки данных из JSON файла'''

        if filename is not None:
            self.filename = filename
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                vacancies_data = json.load(file)
            return vacancies_data
        except (IOError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Ошибка при чтении вакансий из JSON: {str(e)}")


class HH_vacancies:

    def __init__(self, name, vacancy_url, salary, requirements):
        self.salary = salary
        self.name = name
        self.vacancy_url = vacancy_url
        self.requirements = requirements

    def __str__(self):
        return f"{self.name} ({self.salary}) - {self.vacancy_url}"


# class Superjob_API(JobSitesAPI):
#     def __init__(self, keyword, page=0):
#         self.url = "https://api.superjob.ru/2.0/vacancies/"
#         self.params = {
#             "keywords": keyword,
#             "page": page
#         }
#
#     def get_requests(self):
#         headers = {"X-Api-App-Id": os.environ("SUPERJOB_API_KEY")}
#         return requests.get(self.url, headers=headers, params=self.params)
#
