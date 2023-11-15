import json
import os
import requests
from abc import ABC, abstractmethod


def highlight_vacancy(func):
    def wrapper(vacancy_instance):
        print("=" * 40)
        func(vacancy_instance)
        print("=" * 40)
        print('')

    return wrapper


class HH_vacancies:

    def __init__(self, vacancy_data):
        self.__salary = f"{vacancy_data.get('salary', {}).get('from', '')} - {vacancy_data.get('salary', {}).get('to', '')} " \
                        f"{vacancy_data.get('salary', {}).get('currency', '')}" if vacancy_data.get('salary') else ''
        self.__name = vacancy_data.get('name', '')
        self.__vacancy_url = vacancy_data.get('alternate_url', '')
        self.__requirement = vacancy_data.get('snippet', {}).get('requirement', '')

    def get_name(self):
        return self.__name

    def get_vacancy_url(self):
        return self.__vacancy_url

    def get_salary(self):
        return self.__salary

    def get_requirement(self):
        return self.__requirement

class SuperjobVacancies:

    def __init__(self, vacancy_data):
        self.__salary = f"{vacancy_data.get('payment_from', '')} - {vacancy_data.get('payment_to', '')} " \
                        f"{vacancy_data.get('currency', '')}" if vacancy_data.get('payment_from') else ''
        self.__name = vacancy_data.get('profession', '')
        self.__vacancy_url = vacancy_data.get('link', '')
        self.__requirement = vacancy_data.get('candidat', '')

    def get_name(self):
        return self.__name

    def get_vacancy_url(self):
        return self.__vacancy_url

    def get_salary(self):
        return self.__salary

    def get_requirement(self):
        return self.__requirement


    @highlight_vacancy
    def display(self):
        print(f"Название вакансии: {self.__name}")
        print(f"Зарплата: {self.__salary}")
        print(f"Ссылка на вакансию: {self.__vacancy_url}")
        print(f"Требования: {self.__requirement}")




# class Superjob_API(JobSitesAPI):
#     def __init__(self, keyword, page=0):
#         self.url = "https://api.superjob.ru/2.0/vacancies/"
#         self.params = {
#             "keywords": keyword,
#             "page": page
#         }
#
#     def get_vacancies(self):
#         headers = {"X-Api-App-Id": os.environ("SUPERJOB_API_KEY")}
#         return requests.get(self.url, headers=headers, params=self.params)
#
