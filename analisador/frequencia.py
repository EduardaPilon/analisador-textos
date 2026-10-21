
from analisador.texto import preparar_palavra


def contar_ocorrencias(texto, palavra_buscada):
    total_ocorrencias = 0
    palavra_buscada = preparar_palavra(palavra_buscada)

    for palavra_atual in texto.split():
        palavra_atual = preparar_palavra(palavra_atual)

        if palavra_atual == palavra_buscada:
            total_ocorrencias += 1

    return total_ocorrencias