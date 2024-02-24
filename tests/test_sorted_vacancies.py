import pytest
from src.HHConection import Get_had_hanter
from src.sorted_vacancies import sortedVacancy


@pytest.fixture
def get_head_hunter():
    return Get_had_hanter("python", 1)


def test_sorted_vacancy():
    """
    Проверка на наличие 2х экземпляров класса
    """
    r = sortedVacancy()
    assert r.hh_sorted == []
    assert r.date_format == None


def test_sorted_vacancies_hh():
    """
     Проверка на работоспособность сортировки вакансии
    """
    r = sortedVacancy()
    assert r.sorted_vacancies_hh == [{'city': 'Оренбург',
                                      'date': '29.01.2024',
                                      'name': 'Стажер-разработчик Python',
                                      'payment_1': 50000,
                                      'payment_2': 50000,
                                      'skill_1': 'Отличные коммуникативные навыки. Любовь к коду. Быть активным и '
                                                 'внедрять эффективные решения.',
                                      'skill_2': 'Внедрять новые инженерные решения. Поддерживать текущий проект. '
                                                 'Разработка десктоп ПО по нашим лекалам.'}]



def test_error_vacancies_sorted():
    """
    Проверка на наличие ошибок
    """
    with pytest.raises(TypeError):
        sortedVacancy(100)
