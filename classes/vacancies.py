import json
import os
import requests
from abc import ABC, abstractmethod


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
#     def get_vacancies(self):
#         headers = {"X-Api-App-Id": os.environ("SUPERJOB_API_KEY")}
#         return requests.get(self.url, headers=headers, params=self.params)
#
