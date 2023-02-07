from src.limpar_string.limpa import remover_espacos_em_branco

def test_remover_espacos():

    texto = "qualquer string"

    validacao = remover_espacos_em_branco(texto)

    assert (' ' in validacao) == False