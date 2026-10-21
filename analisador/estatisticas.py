from analisador.texto import remover_acentos, preparar_palavra


def contar_vogais_consoantes(texto):
    vogais = ['a', 'e', 'i', 'o', 'u']

    total_consoantes = 0
    total_vogais = 0

    frequencia_vogais = {
        'a': 0,
        'e': 0,
        'i': 0,
        'o': 0,
        'u': 0
    }

    for palavra_atual in texto.split():
        for letra_atual in palavra_atual:
            letra_atual = remover_acentos(letra_atual.lower())

            if letra_atual.isalpha() and letra_atual not in vogais:
                total_consoantes += 1

            if letra_atual in vogais:
                total_vogais += 1
                frequencia_vogais[letra_atual] += 1

    return {
        'total_consoantes': total_consoantes,
        'total_vogais': total_vogais,
        'frequencia_vogais': frequencia_vogais
    }


def contar_palavras(texto):
    lista_palavras = texto.split()
    total_palavras = len(lista_palavras)

    return total_palavras


def encontrar_maior_palavra(texto):
    maior_palavra = ""
    tamanho_maior_palavra = 0

    for palavra_atual in texto.split():
        palavra_atual = preparar_palavra(palavra_atual)

        if len(palavra_atual) > tamanho_maior_palavra:
            maior_palavra = palavra_atual
            tamanho_maior_palavra = len(palavra_atual)

    return maior_palavra, tamanho_maior_palavra


def contar_palavras(texto):
    palavras = texto.split()
    return len(palavras)


def encontrar_maior_palavra(texto):
    maior_palavra = ""
    maior_quant = 0

    for palavra in texto.split():
        palavra = palavra.lower().strip(".,!?;:")

        if len(palavra) > maior_quant:
            maior_palavra = palavra
            maior_quant = len(palavra)

    return maior_palavra, maior_quant
