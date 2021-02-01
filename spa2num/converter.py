import re


class Spa2NumLexiconException(Exception):
    pass


class Spa2NumSyntaxException(Exception):
    pass


def _valid_lexicon(x):
    # TODO: function that check allowed tokens.
    return True


def _valid_syntax(x):
    # TODO: function that check syntax rules for an spelled spanish number.
    return True

def _process_words(s):
    words = s.split()
    total = 0
    carry = 0
    for word in words:
        word = int(word)
        if word == 1000:
            if carry == 0:
                carry = 1000
            else:
                carry = carry*1000
        elif word == 1000000:
            if carry == 0:
                total = total + 1000000
            else:
                total = total + carry*1000000
            carry = 0
        else:
            carry = carry + word
    return total + carry


def to_number(x):
    """
    Allows you to translate to integer numerical words spelled in spanish.

    Text must be previously cleaned & removed extraneous words or symbols.
    Quantities MUST be written in a correct Spanish.
    The upper limit is up to the millions range. No decimal supported.

    Args:
        An spanish spelled number.

    Returns:
        Integer translated from the Spanish text string

    """

    if not _valid_lexicon(x):
        raise Spa2NumLexiconException("not allowed tokens found")  # TODO: show which tokens are not allowed

    if not _valid_syntax(x):
        raise Spa2NumSyntaxException("invalid sintax found")

    x = x.lower()
    x = re.sub("cero", " 0 ", x)
    x = re.sub("once", " 11 ", x)
    x = re.sub("doce", " 12 ", x)
    x = re.sub("trece", " 13 ", x)
    x = re.sub("catorce", " 14 ", x)
    x = re.sub("quince", " 15 ", x)
    x = re.sub("dieciseis", " 16 ", x)
    x = re.sub("diecisiete|diez y siete", " 17 ", x)
    x = re.sub("dieciocho", " 18 ", x)
    x = re.sub("diecinueve", " 19 ", x)
    x = re.sub("veinte|veinti", " 20 ", x)
    x = re.sub("treinta", " 30 ", x)
    x = re.sub("cuarenta", " 40 ", x)
    x = re.sub("cincuenta", " 50 ", x)
    x = re.sub("sesenta", " 60 ", x)
    x = re.sub("setenta", " 70 ", x)
    x = re.sub("ochenta", " 80 ", x)
    x = re.sub("noventa", " 90 ", x)
    x = re.sub("doscientos", " 200 ", x)
    x = re.sub("trescientos", " 300 ", x)
    x = re.sub("cuatrocientos", " 400 ", x)
    x = re.sub("quinientos", " 500 ", x)
    x = re.sub("seiscientos", " 600 ", x)
    x = re.sub("setecientos", " 700 ", x)
    x = re.sub("ochocientos", " 800 ", x)
    x = re.sub("novecientos", " 900 ", x)
    x = re.sub("uno|un|ún", " 1 ", x)
    x = re.sub("dos|dós", " 2 ", x)
    x = re.sub("tres|trés", " 3 ", x)
    x = re.sub("cuatro", " 4 ", x)
    x = re.sub("cinco", " 5 ", x)
    x = re.sub("seis|séis", " 6 ", x)
    x = re.sub("siete", " 7 ", x)
    x = re.sub("ocho", " 8 ", x)
    x = re.sub("nueve", " 9 ", x)
    x = re.sub("millones", " 1000000 ", x)
    x = re.sub("millon|millón", " 1000000 ", x)
    x = re.sub("mil", " 1000 ", x)
    x = re.sub("ciento", " 100 ", x)
    x = re.sub("cien", " 100 ", x)
    x = re.sub("diez", " 10 ", x)
    x = re.sub("un", " 1 ", x)
    x = re.sub("y|Y", "", x)
    return _process_words(x)
