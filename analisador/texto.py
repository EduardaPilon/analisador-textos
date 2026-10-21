import unicodedata

def remover_acentos(texto):
    texto_normalizado = unicodedata.normalize('NFD', texto)
    return ''.join(
        caractere for caractere in texto_normalizado
        if unicodedata.category(caractere) != 'Mn'
    )

def normalizar_texto(texto):
    return texto.strip().lower()


def preparar_palavra(palavra):
    return palavra.strip(".,!?;:").lower()