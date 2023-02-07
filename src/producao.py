from src.limpar_string.limpa import tratar_texto, conteudo_valido

def valida_palindromo(texto):
    
    if not conteudo_valido(texto):
        print("AVERIGUE A QUALIDADE DE SEU TEXTO A SER VERIFICADO:", texto)
        return False

    validacao = tratar_texto(texto)

    return validacao == validacao[::-1]


