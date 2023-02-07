import unicodedata

def remover_espacos_em_branco(texto):
    return texto.replace(" ", "")

def caixa_baixa(texto):
    return texto.lower()

def remover_acentos(texto):
    texto = ''.join(ch for ch in unicodedata.normalize('NFKD', texto)
                        if not unicodedata.combining(ch))
    return texto