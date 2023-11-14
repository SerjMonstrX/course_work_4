import json
from abc import ABC, abstractmethod


class JsonHandler(ABC):

    @abstractmethod
    def save_to_json(self, vacancies_data):
        pass

    @abstractmethod
    def load_from_json(self, filename):
        pass


class HeadhunterJson(JsonHandler):

    def __init__(self, filename='hh_data.json'):
        self.filename = filename

    def save_to_json(self, vacancies_data):
        """ Функция для сохранения данных в JSON файл"""

        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump(vacancies_data, file, ensure_ascii=False, indent=2)
            print(f"Вакансии успешно сохранены в файл {self.filename}")
        except IOError as e:
            raise RuntimeError(f"Ошибка при записи вакансий в JSON: {str(e)}")


    def load_from_json(self):
        """ Функция для загрузки данных из JSON файла"""

        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                vacancies_data = json.load(file)
            return vacancies_data
        except (IOError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Ошибка при чтении вакансий из JSON: {str(e)}")
