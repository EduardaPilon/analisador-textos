
def contar_ocorrencias(texto, palavra_escolhida):
    quantidade = 0

    for palavra in texto.split():
        palavra = palavra.lower().strip(".,!?;:")

        if palavra == palavra_escolhida.lower():
            quantidade += 1

    return quantidade
