from src.functions import print_hh_vacancies, print_superjob_vacancies


print('Приветствуем вас. Наш сервис поможет вам подобрать вакансию по запросу.')
user_vacancy_text = input("""Мы работаем с сайтами:
1 - headhunter.ru 
2 - superjob.ru 
Введите номер сайта 1 или 2 для поиска вакансий: """)

if user_vacancy_text == '1':
    print_hh_vacancies()
elif user_vacancy_text == '2':
    print_superjob_vacancies()
