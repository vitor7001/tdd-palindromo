import unicodedata

def tratar_texto(texto):
    texto_tratado = remover_espacos_em_branco(texto)
    texto_tratado = caixa_baixa(texto_tratado)
    texto_tratado = remover_acentos_nas_letras(texto_tratado)
    texto_tratado = remover_acentos_na_frase(texto_tratado)
    return texto_tratado
    
def conteudo_valido(texto):
    if not texto:
        return False
    
    if classe_diferente_de_string(texto):
        return False

    return True

def classe_diferente_de_string(texto):
    if not isinstance(texto, str):
        return True

    return False    

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
    texto = texto.replace('’', '')
    texto = texto.replace('\'', '')
    return texto
