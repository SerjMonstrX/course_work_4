from classes.vacancies import HeadhunterVacancies, SuperjobVacancies
from classes.jsonhandler import HeadhunterJson, SuperjobJson
from classes.api import HeadhunterAPI, SuperjobAPI


def print_headhunter_vacancies():
    user_vacancy_text = input('Введите текст для поиска вакансий: ')

    # Цикл для выбора количества просматриваемых страниц для поиска
    while True:
        try:
            num_pages = int(input("Введите число страниц для просмотра: "))
            if num_pages > 0:
                break  # Если ввод корректен, выходим из цикла
            else:
                print("Ошибка! Введите число больше 0.")
        except ValueError:
            print("Ошибка! Введите число.")

    all_headhunter_vacancies_data = []

    for page in range(num_pages):
        headhunter_response = HeadhunterAPI(user_vacancy_text, page)
        hh_data = headhunter_response.get_vacancies()
        all_headhunter_vacancies_data.extend(hh_data)

    hh_json = HeadhunterJson()
    hh_json.save_to_json(all_headhunter_vacancies_data)  # Запись вакансий в файл JSON

    while True:
        sorted_by_salary = input("""Список вакансий подготовлен. Отсортировать вакансии по убыванию зарплаты? (без указания ЗП выведены не будут)
            1 - Да
            2 - Нет
            Введите ответ 1 или 2 для сортировки вакансий по зарплате:""")
        if sorted_by_salary == '1':
            hh_loaded_data = hh_json.load_from_json_sorted_by_salary()  # Загрузка вакансий из файла JSON
            break  # Если ввод корректен, выходим из цикла
        elif sorted_by_salary == '2':
            hh_loaded_data = hh_json.load_from_json()  # Загрузка вакансий из файла JSON
            break  # Если ввод корректен, выходим из цикла
        else:
            print("Ошибка! Введите 1 или 2.\n")

    vacancy_instances = [HeadhunterVacancies(vacancy_data) for vacancy_data in hh_loaded_data]

    for vacancy in vacancy_instances:
        vacancy.display()


def print_superjob_vacancies():
    user_vacancy_text = input('Введите текст для поиска вакансий: ')

    # Цикл для выбора количества просматриваемых страниц для поиска
    while True:
        try:
            num_pages = int(input("Введите число просматриваемых страниц: "))
            if num_pages > 0:
                break  # Если ввод корректен, выходим из цикла
            else:
                print("Ошибка! Введите число больше 0.")
        except ValueError:
            print("Ошибка! Введите число.")

    superjob_response = SuperjobAPI(user_vacancy_text, 1)
    superjob_data = superjob_response.get_vacancies()

    superjob_json = SuperjobJson()
    superjob_json.save_to_json(superjob_data)  # Запись вакансий в файл JSON

    while True:
        sorted_by_salary = input("""Список вакансий подготовлен. Отсортировать вакансии по убыванию зарплаты? (без указания ЗП выведены не будут)
            1 - Да
            2 - Нет
            Введите ответ 1 или 2 для сортировки вакансий по зарплате:""")
        if sorted_by_salary == '1':
            superjob_loaded_data = superjob_json.load_from_json_sorted_by_salary()  # Загрузка вакансий из файла JSON
            break  # Если ввод корректен, выходим из цикла
        elif sorted_by_salary == '2':
            superjob_loaded_data = superjob_json.load_from_json()  # Загрузка вакансий из файла JSON
            break  # Если ввод корректен, выходим из цикла
        else:
            print("Ошибка! Введите 1 или 2.\n")

    superjob_vacancy_instances = [SuperjobVacancies(vacancy_data) for vacancy_data in superjob_loaded_data]

    for vacancy in superjob_vacancy_instances:
        vacancy.display()
        