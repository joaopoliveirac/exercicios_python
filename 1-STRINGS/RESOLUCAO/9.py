# 9. Contar Palavras em uma Frase
# Peça ao usuário para digitar uma frase e exiba a quantidade de palavras que ela contém.

frase = input('digite uma frase: ')
frase_lista = frase.split()
print(len(frase_lista))
