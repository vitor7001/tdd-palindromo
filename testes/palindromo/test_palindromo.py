from src.producao import valida_palindromo


def test_palindromo_valido():
    assert valida_palindromo("ovo") == True


def test_palindromo_invalido():
    assert valida_palindromo("qualquer texto") == False


def test_casos_validos():
    lista_casos_validos = [
        "Rotator",
        "bob",
        "madam",
        "mAlAyAlam",
        "1",
        "Able was I, ere I saw Elba",
        "Madam I’m Adam",
        "Step on no pets.",
        "Top spot!",
        "02/02/2020",
        "Socorram-me subi no ônibus em marrocos",
    ]

    for item in lista_casos_validos:
        assert valida_palindromo(item) == True


def test_casos_invalidos():
    lista_casos_invalidos = [
        "xyz",
        "elephant",
        "Country",
        "Top . post!",
        "Wonderful-fool",
        "Wild imagination!",
    ]

    for item in lista_casos_invalidos:
        assert valida_palindromo(item) == False