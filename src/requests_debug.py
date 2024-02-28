from src.user_froms import UserForm


class RequestDebug(UserForm):
    """
    класс поиска ошибок вакансий

    """

    def __init__(self):
        self.top_n = None
        self.search_query = None

    def user_input_int(self):
        """
        метод поиска ошибок ввода количества вакансий
        :return: int
        """
        self.top_n = input("Введите колличество вакансий:\n ").strip()
        if self.top_n.isalpha():
            raise ValueError("Надо вводить число")
        if self.top_n == "":
            raise AttributeError("Количество не может быть пустой строкой")
        if int(self.top_n) > 100:
            self.top_n = 100
        return int(self.top_n)

    def user_input_str(self):
        """
        метод ввода ошибок вакансий
        :return:
        """
        self.search_query = input("Введите поисковой запрос:\n ").strip()
        if self.search_query.isdigit():
            raise TypeError("Запрос не может быть числом")
        if self.search_query == "":
            raise AttributeError("Название не должно быть пустой строки")
        else:
            return self.search_query


if __name__ == '__main__':
    r = RequestDebug()
    print(r.user_input_str())
