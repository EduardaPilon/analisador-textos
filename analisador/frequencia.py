def contar_ocorrencias(texto, palavra_buscada):
    total_ocorrencias = 0

    for palavra_atual in texto.split():
        palavra_atual = palavra_atual.lower().strip(".,!?;:")

        if palavra_atual == palavra_buscada.lower():
            total_ocorrencias += 1

    return total_ocorrencias

