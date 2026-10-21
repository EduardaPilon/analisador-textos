
from analisador.texto import remover_acentos


def contar_vogais_consoantes(texto):
    vogais = ['a', 'e', 'i', 'o', 'u']

    consoantes = 0
    quant = 0

    contagem_vogais = {
        'a': 0,
        'e': 0,
        'i': 0,
        'o': 0,
        'u': 0
    }

    for palavra in texto.split():
        for letra in palavra:
            letra = remover_acentos(letra.lower())

            if letra.isalpha() and letra not in vogais:
                consoantes += 1

            if letra in vogais:
                quant += 1
                contagem_vogais[letra] += 1

    return {
        'consoantes': consoantes,
        'vogais': quant,
        'contagem_vogais': contagem_vogais
    }


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
