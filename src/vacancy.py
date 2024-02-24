class Vacancy:
    """
    класс для перезаписи приватных атрибутов
    для класса Get_had_hanter, и методы str и repr
    """

    def __init__(self, name, page):
        self.__name = name
        self.__page = page

    @property
    def name(self):
        return self.__name

    @property
    def page(self):
        return self.__page

    def __str__(self):
        return f"{self.__name}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__name, self.__page})"
