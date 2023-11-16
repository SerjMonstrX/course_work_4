import json
import os
import requests
from abc import ABC, abstractmethod
from src.variables import SUPERJOB_API_KEY

class JobSitesAPI(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass


class HeadhunterAPI(JobSitesAPI):
    def __init__(self, keyword, page=0):
        self.url = "https://api.hh.ru/vacancies"
        self.params = {
            "text": keyword,
            "page": page
        }
        self.filename = 'hh_data.json'  # Используем относительный путь

    def get_vacancies(self):
        """ Функция для запроса данных с сайта HH по API"""

        try:
            response = requests.get(self.url, params=self.params)
            response.raise_for_status()  # Это вызовет исключение, если код состояния не 200

            try:
                vacancies_data = response.json().get('items', [])
            except json.JSONDecodeError as json_error:
                print(f"Ошибка декодирования JSON: {json_error}")
                vacancies_data = []
            print(vacancies_data)
            return vacancies_data

        except requests.RequestException as e:
            print(f'Ошибка {response.status_code}: {response.text}')
            raise RuntimeError(f"Не удалось получить вакансии с HH: {str(e)}")



class SuperjobAPI(JobSitesAPI):
    def __init__(self, keywords, page=1):
        self.url = "https://api.superjob.ru/2.0/vacancies/"
        self.params = {
            "keyword": keywords,
            "page": page
        }
        self.filename = 'superjob_data.json'  # Используем относительный путь

    def get_vacancies(self):
        """ Функция для запроса данных с сайта HH по API"""
        headers = {"X-Api-App-Id": SUPERJOB_API_KEY.lstrip().rstrip()}
        try:
            response = requests.get(self.url, headers=headers, params=self.params)
            response.raise_for_status()  # Это вызовет исключение, если код состояния не 200
            try:
                vacancies_data = response.json().get('objects', [])
            except json.JSONDecodeError as json_error:
                print(f"Ошибка декодирования JSON: {json_error}")
                vacancies_data = []
            return vacancies_data

        except requests.RequestException as e:
            print(f'Ошибка {response.status_code}: {response.text}')
            raise RuntimeError(f"Не удалось получить вакансии с Superjob: {str(e)}")

