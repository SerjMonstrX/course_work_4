from classes.vacancies import HH_vacancies, SuperjobVacancies
from classes.jsonhandler import HeadhunterJson, SuperjobJson
from classes.api import HeadhunterAPI, SuperjobAPI
def print_hh_vacancies():
    user_vacancy_text = input('Введите текст для поиска вакансий: ')

    # Цикл для выбора количества просматриваемых страниц для поиска, если не число, то пользователь вводит значение заново
    while True:
        try:
            num_pages = int(input("Введите число вакансий: "))
            if num_pages > 0:
                break  # Если ввод корректен, выходим из цикла
            else:
                print("Ошибка! Введите число больше 0.")
        except ValueError:
            print("Ошибка! Введите число.")

    all_hh_vacancies_data = []

    for page in range(num_pages):
        Headhunter_response = HeadhunterAPI(user_vacancy_text, page)
        hh_data = Headhunter_response.get_vacancies()
        all_hh_vacancies_data.extend(hh_data)

    hh_json = HeadhunterJson()
    hh_json.save_to_json(all_hh_vacancies_data)  # Запись вакансий в файл JSON
    hh_loaded_data = hh_json.load_from_json_sorted_by_salary()  # Загрузка вакансий из файла JSON

    # Пример инициализации объекта Vacancy из первой записи в данных

    vacancy_instances = [HH_vacancies(vacancy_data) for vacancy_data in hh_loaded_data]

    for vacancy in vacancy_instances:
        vacancy.display()


def print_superjob_vacancies():
    user_vacancy_text = input('Введите текст для поиска вакансий: ')

    # Цикл для выбора количества просматриваемых страниц для поиска, если не число, то пользователь вводит значение заново
    while True:
        try:
            num_pages = int(input("Введите число: "))
            if num_pages > 0:
                break  # Если ввод корректен, выходим из цикла
            else:
                print("Ошибка! Введите число больше 0.")
        except ValueError:
            print("Ошибка! Введите число.")

    Superjob_response = SuperjobAPI(user_vacancy_text, 1)
    superjob_data = Superjob_response.get_vacancies()

    superjob_json = SuperjobJson()
    superjob_json.save_to_json(superjob_data)  # Запись вакансий в файл JSON
    superjob_loaded_data = superjob_json.load_from_json()  # Загрузка вакансий из файла JSON

    # Пример инициализации объекта Vacancy из первой записи в данных

    superjob_vacancy_instances = [SuperjobVacancies(vacancy_data) for vacancy_data in superjob_loaded_data]

    for vacancy in superjob_vacancy_instances:
        vacancy.display()