from palindrommo.palindromo import valida_palindromo

def test_palindromo_valido():
    assert valida_palindromo("qualquer texto") == True

def test_palindromo_invalido():
    assert valida_palindromo("qualquer texto") == False