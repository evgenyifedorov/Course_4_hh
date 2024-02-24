from abc import ABC, abstractmethod


class vacancy_API(ABC):
    """
    создан абстрактный класс для вакансий и его метода
    """

    @abstractmethod
    def get_vacancy(self):
        pass
