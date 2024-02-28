import pytest
from src.hh_conection import GetHadHanter
from src.sorted_vacancies import Sortedvacancy


@pytest.fixture
def get_head_hunter():
    return GetHadHanter("python", 1)


def test_sorted_vacancy():
    """
    Проверка на наличие 2х экземпляров класса
    """
    r = Sortedvacancy()
    assert r.hh_sorted == []
    assert r.date_format == None


def test_error_vacancies_sorted():
    """
    Проверка на наличие ошибок
    """
    with pytest.raises(TypeError):
        Sortedvacancy(100)
