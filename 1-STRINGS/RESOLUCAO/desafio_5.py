# 5. Encontrar a Maior Palavra em um Texto
# Escreva uma função que receba uma string longa e retorne a maior palavra presente nela.
def maior_palavra(texto):
    texto_lista = texto.split()
    qtde_caracter = []

    for palavra in texto_lista:
        qtde_caracter.append(len(palavra))

    return print(max(qtde_caracter))


maior_palavra('JOAO PEDRO OLIVEIRA CARVALHOAHAOSA')

#conferindo com outras respotas, descobri que tem como usar essa função: max(palavras, key=len) que conta diretamente a quantidade de caracter dos itens da lista