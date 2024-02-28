from abc import ABC, abstractmethod


class VacancyApi(ABC):
    """
    создан абстрактный класс для вакансий и его метода
    """

    @abstractmethod
    def get_vacancy(self):
        pass
