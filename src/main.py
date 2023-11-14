from classes.vacancies import HH_vacancies
from classes.jsonhandler import HeadhunterJson
from classes.api import HH_API

hh_api = HH_API('python')
hh_data = hh_api.get_vacancies()

hh_json = HeadhunterJson()
hh_json.save_to_json(hh_data) #Запись вакансий в файл JSON
loaded_data = hh_json.load_from_json()  #Загрузка вакансий из файла JSON

# Пример инициализации объекта Vacancy из первой записи в данных

vacancy_instance = [HH_vacancies(
    name=vacancy_data.get('name', ''),
    vacancy_url=vacancy_data.get('alternate_url', ''),
    salary=f"{vacancy_data.get('salary', {}).get('from', '')} - {vacancy_data.get('salary', {}).get('to', '')} {vacancy_data.get('salary', {}).get('currency', '')}" if vacancy_data.get('salary') else '',
    requirements=vacancy_data.get('snippet', {}).get('requirements', '')
) for vacancy_data in loaded_data]

for vacancy in vacancy_instance:
    print(vacancy)

# Superjob_response = Superjob('python')


# print(Superjob_response.get_vacancies())