import unicodedata

def remover_espacos_em_branco(texto):
    return texto.replace(" ", "")

def caixa_baixa(texto):
    return texto.lower()

def remover_acentos_nas_letras(texto):
    texto = ''.join(ch for ch in unicodedata.normalize('NFKD', texto)
                        if not unicodedata.combining(ch))
    return texto

def remover_acentos_na_frase(texto):
    texto = texto.replace('-', '')
    texto = texto.replace('.', '')
    texto = texto.replace('!', '')
    texto = texto.replace(',', '')
    texto = texto.replace('/', '')
    return texto
