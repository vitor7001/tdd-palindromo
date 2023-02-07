from src.limpar_string.limpa import *

def test_remover_espacos():

    texto = "qualquer string"

    validacao = remover_espacos_em_branco(texto)

    assert (' ' in validacao) == False

def test_caixa_baixa():

    texto = "QUALQUER TEXTO"

    validacao = caixa_baixa(texto)

    assert validacao == "qualquer texto"