from src.requests_debug import RequestDebug
from src.debug_user_json import DebugUser
from src.sorted_vacancies import Sortedvacancy
from src.hh_conection import GetJson


class UserInteractionHeadHunter(RequestDebug):
    """
    Класс взаимодействия пользователя с сайтом HeadHunter
    """
    def user_search(self):
        search_query = self.user_input_str()
        top_n = self.user_input_int()
        result_search = GetJson(search_query, top_n)
        result_search.get_json()



class UserInteractionJson(DebugUser):
    """
    Класс взаимодействия пользователя с файлом Json
    """
    def json_user_search(self):
        """
        Метод сортировки вакансий Json файла
        """
        vacancies_list = []
        json_file = Sortedvacancy()
        json_vacancies = json_file.sorted_vacancies_hh
        payment = self.user_input_int()
        city = self.user_input_str()
        for vacancies in json_vacancies:
            if payment > vacancies["payment_1"]:
                continue
            if city == vacancies["city"]:
                vacancies_list.append(vacancies)
            if city == "":
                vacancies_list.append(vacancies)
        for result in vacancies_list:
            print(f"Город: {result['city']}\nДата публикации: {result['date']}\n"
                  f"Должность: {result['name']}\nТребование: {result['skill_1']}\n"
                  f"Ответственность: {result['skill_2']}\nЗарплата от {result['payment_1']}\n"
                  f"Зарплата до {result['payment_2']}\n")
        if len(vacancies_list) == 0:
            print(f'Результатов 0')



if __name__ == '__main__':
    r = UserInteractionHeadHunter()
    r.user_search()


