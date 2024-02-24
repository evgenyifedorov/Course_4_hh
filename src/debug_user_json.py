from src.user_froms import UserForm


class DebugUser(UserForm):
    """
    класс ввода ошибок зарплаты и города
    """

    payment = None
    city = None


    def user_input_int(self):
        """
        ошибки на ввод зарплаты
        :return:
        """
        self.payment = input("Введите минимальную зарплату:\n ")

        if self.payment.isalpha():
            raise ValueError("Надо вводить число")
        if self.payment == " ":
            self.payment = 0
        return int(self.payment)


    def user_input_str(self):
        """
        ошибка ввода города
        :return:
        """
        self.city = input("Введите город:\n ").title()
        if self.city.isdigit():
            raise TypeError("Название введите буквами:\n ")
        return self.city


if __name__ == '__main__':
    r = DebugUser()
    print(r.user_input_str())

