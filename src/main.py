from classes.vacancies import HH_vacancies, SuperjobVacancies
from classes.jsonhandler import HeadhunterJson, SuperjobJson
from classes.api import HeadhunterAPI, SuperjobAPI


print('Приветствуем вас. Наш сервис поможет вам подобрать вакансию по запросу.')
user_vacancy_text = input('Введите текст для поиска вакансий: ')

#Цикл для выбора количества просматриваемых страниц для поиска, если не число, то пользователь вводит значение заново
while True:
    try:
        num_pages = int(input("Введите число: "))
        if num_pages > 0:
            break  # Если ввод корректен, выходим из цикла
        else:
            print("Ошибка! Введите число больше 0.")
    except ValueError:
        print("Ошибка! Введите число.")


# all_vacancies_data = []
#
# for page in range(num_pages):
#     HeadhunterAPI = HeadhunterAPI(user_vacancy_text, page)
#     hh_data = HeadhunterAPI.get_vacancies()
#     all_vacancies_data.extend(hh_data)
#
# hh_json = HeadhunterJson()
# hh_json.save_to_json(all_vacancies_data)  # Запись вакансий в файл JSON
# hh_loaded_data = hh_json.load_from_json_sorted_by_salary()  # Загрузка вакансий из файла JSON
#
# # Пример инициализации объекта Vacancy из первой записи в данных
#
# vacancy_instances = [HH_vacancies(vacancy_data) for vacancy_data in hh_loaded_data]
#
# for vacancy in vacancy_instances:
#     vacancy.display()

Superjob_var = SuperjobAPI(user_vacancy_text, 1)
superjob_data = Superjob_var.get_vacancies()

superjob_json = SuperjobJson()
superjob_json.save_to_json(superjob_data)  # Запись вакансий в файл JSON
superjob_loaded_data = superjob_json.load_from_json()  # Загрузка вакансий из файла JSON

# Пример инициализации объекта Vacancy из первой записи в данных

superjob_vacancy_instances = [SuperjobVacancies(vacancy_data) for vacancy_data in superjob_loaded_data]

for vacancy in superjob_vacancy_instances:
    vacancy.display()