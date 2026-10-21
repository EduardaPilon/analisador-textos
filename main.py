
from analisador.estatisticas import (
    contar_vogais_consoantes,
    contar_palavras,
    encontrar_maior_palavra
)
from analisador.frequencia import contar_ocorrencias


texto = """
Python é uma linguagem de programação de alto nível conhecida por sua sintaxe simples, legível e produtiva. Criada com foco na clareza do código, ela é amplamente utilizada no desenvolvimento web, automação de tarefas, análise de dados, inteligência artificial, machine learning e computação científica. Seu vasto ecossistema de bibliotecas, como NumPy, Pandas, TensorFlow e PyTorch aliado à grande comunidade de desenvolvedores, faz do Python uma das linguagens mais populares e versáteis do mundo, sendo uma excelente escolha tanto para iniciantes quanto para projetos profissionais de alta complexidade.
"""

palavra_escolhida = input(
    "Escreva uma palavra para saber quantas vezes ela aparece no texto: "
)

resultado = contar_vogais_consoantes(texto)
total_palavras = contar_palavras(texto)
maior_palavra, maior_quant = encontrar_maior_palavra(texto)
quantidade_palavra = contar_ocorrencias(texto, palavra_escolhida)

print(
    f"O texto tem {resultado['consoantes']} consoantes "
    f"e {resultado['vogais']} vogais.\n"
)

for vogal, quantidade in resultado['contagem_vogais'].items():
    print(f"Letra {vogal}: {quantidade}")

print(
    f"O texto tem {total_palavras} palavras. "
    f"A maior palavra é {maior_palavra}, com {maior_quant} letras."
)

print(
    f"A palavra {palavra_escolhida} aparece "
    f"{quantidade_palavra} vez(es) no texto."
)
