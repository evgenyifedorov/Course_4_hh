import pytest
from src.vacancy import Vacancy


@pytest.fixture
def vacancy():
    return Vacancy("python", 1)


def test_str(vacancy):
    """
    Проверка метода str
    """
    assert str(vacancy) == "python"


def test_repr(vacancy):
    """
    Проверка метода repr
    """
    assert repr(vacancy) == "Vacancy(('python', 1))"


def test_name_error(vacancy):
    """
    Проверка на наличие ошибок в названии
    """
    with pytest.raises(AttributeError):
        vacancy.name = "word"


def test_page_error(vacancy):
    """
    Проверка на наличие ошибок в количестве
    """
    with pytest.raises(AttributeError):
        vacancy.page = 1
