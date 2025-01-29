# 1. Codificador de Strings (Cifra de César)
# Implemente uma função que codifique uma string usando a Cifra de César, deslocando cada letra um número específico de posições no alfabeto.



alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def cifra_cesar (alfabeto):
    senha = input('informe sua senha')
    senha_codficada = ''
    for caracter in senha:
        posicao = alfabeto.index(caracter) + 3
        senha_codficada += alfabeto[posicao]
    return print(senha_codficada)

cifra_cesar(alfabeto)

    