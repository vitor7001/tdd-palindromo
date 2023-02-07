from src.limpar_string.limpa import *

def test_tratar_texto():
    texto = "Able was I, ere I saw Elba"

    validacao = tratar_texto(texto)

    assert validacao == "ablewasiereisawelba"

def test_erro_se_receber_string_vazia():

    texto = ""

    validacao = conteudo_valido(texto)

    assert validacao == False

def test_valido_se_receber_string_com_conteudo():
    texto = "texto"

    validacao = conteudo_valido(texto)

    assert validacao == True

def test_remover_espacos():

    texto = "qualquer string"

    validacao = remover_espacos_em_branco(texto)

    assert (' ' in validacao) == False

def test_caixa_baixa():

    texto = "QUALQUER TEXTO"

    validacao = caixa_baixa(texto)

    assert validacao == "qualquer texto"

def test_remover_acentos_nas_letras():
    
    texto = "úm téxto cóm àcéntós"

    validacao = remover_acentos_nas_letras(texto)

    assert validacao == "um texto com acentos"

def test_remover_acentos_na_frase():

    texto = "-esta frase. possui, acentos!"

    validacao = remover_acentos_na_frase(texto)

    assert validacao == 'esta frase possui acentos'