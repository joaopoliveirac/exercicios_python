# 3. Verificar se uma Palavra é um Pangrama
# Um pangrama é uma frase que contém todas as letras do alfabeto pelo menos uma vez.

def verificar_pangrama(frase):
    frase = frase.lower()
    alfabeto = [chr(i) for i in range (97,123)]
    lista_letras = []
    for caracter in frase:
        for letra in alfabeto:
            if letra in frase:
                if letra not in lista_letras:
                    lista_letras.append(letra)
    
    if len(lista_letras) < len(alfabeto):
        return f"NÃO É UM PANGRAMA"
    else:
        return "É UM PANGRAMA"

print(verificar_pangrama('the quick brown fox jumps over the lazy dog'))


def verificar_pangrama_eficiente(frase):
    frase = frase.lower()
    alfabeto = set(chr(i) for i in range (97,123))
    letras = set(frase)
    if alfabeto.issubset(letras):
        return 'É UM PANGRAMA'
    else:
        return 'NAO É UM PANGRAMA'

print(verificar_pangrama_eficiente('the quick brown fox jumps over the lazy dog'))



