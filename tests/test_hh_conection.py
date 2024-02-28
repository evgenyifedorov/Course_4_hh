import pytest
from src.hh_conection import GetHadHanter


@pytest.fixture
def gethadhanter():
    return GetHadHanter("python", 1)


def test_str(gethadhanter):
    """
    Проверка метода str
    """
    assert str(gethadhanter) == "python"


def test_repr(gethadhanter):
    """
    Проверка метода repr
    """
    assert repr(gethadhanter) == 'GetHadHanter(python, 1)'


def test_url(gethadhanter):
    """
    Проверка работоспособности ссылки
    """
    assert gethadhanter.url == "https://api.hh.ru"


def test_error_connection():
    """
    Проверка на наличие ошибок
    """
    with pytest.raises(TypeError):
        GetHadHanter()
