from spa2num.converter import to_number
from num2words import num2words


def test_converter_1():
    for n in range(1, 1000):
        assert to_number(num2words(n, lang="es")) == n


def test_converter_2():
    for n in range(1000, 100000000, 100):
        print(num2words(n, lang="es"))
        assert to_number(num2words(n, lang="es")) == n


def test_converter_3():
    # TODO: Make a suite test with prime numbers
    pass
