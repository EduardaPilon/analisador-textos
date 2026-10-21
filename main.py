
from analisador.estatisticas import (
    contar_vogais_consoantes,
    contar_palavras,
    encontrar_maior_palavra,
    contar_caracteres,
    contar_caracteres_sem_espacos
)
from analisador.frequencia import contar_ocorrencias


texto_analisado = """
Python é uma linguagem de programação de alto nível conhecida por sua sintaxe simples, legível e produtiva. Criada com foco na clareza do código, ela é amplamente utilizada no desenvolvimento web, automação de tarefas, análise de dados, inteligência artificial, machine learning e computação científica. Seu vasto ecossistema de bibliotecas, como NumPy, Pandas, TensorFlow e PyTorch aliado à grande comunidade de desenvolvedores, faz do Python uma das linguagens mais populares e versáteis do mundo, sendo uma excelente escolha tanto para iniciantes quanto para projetos profissionais de alta complexidade.
"""

palavra_buscada = input(
    "Escreva uma palavra para saber quantas vezes ela aparece no texto: "
)

estatisticas_letras = contar_vogais_consoantes(texto_analisado)
total_palavras = contar_palavras(texto_analisado)

maior_palavra, tamanho_maior_palavra = encontrar_maior_palavra(
    texto_analisado
)

total_ocorrencias = contar_ocorrencias(
    texto_analisado,
    palavra_buscada
)
total_caracteres = contar_caracteres(texto_analisado)

total_caracteres_sem_espacos = contar_caracteres_sem_espacos(
    texto_analisado
)














print(
    f"O texto tem {estatisticas_letras['total_consoantes']} consoantes "
    f"e {estatisticas_letras['total_vogais']} vogais.\n"
)

for vogal, quantidade in estatisticas_letras['frequencia_vogais'].items():
    print(f"Letra {vogal}: {quantidade}")

print(
    f"O texto tem {total_palavras} palavras. "
    f"A maior palavra é {maior_palavra}, "
    f"com {tamanho_maior_palavra} letras."
)

print(
    f"A palavra {palavra_buscada} aparece "
    f"{total_ocorrencias} vez(es) no texto."
)

print(f"O texto tem {total_caracteres} caracteres, incluindo espaços.")

print(
    f"O texto tem {total_caracteres_sem_espacos} caracteres "
    "sem contar os espaços."
)