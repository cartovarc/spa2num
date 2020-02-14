from spa2num.converter import to_number
from num2words import num2words
from primesieve import primes


def test_converter_1():
    for n in range(0, 1000):
        assert to_number(num2words(n, lang="es")) == n


def test_converter_2():
    primes_test = primes(1000000)
    for n in primes_test:
        assert to_number(num2words(n, lang="es")) == n


def test_converter_3():
    primes_test = primes(990000000, 999999999)
    for n in primes_test:
        assert to_number(num2words(n, lang="es")) == n
