# 5. Substituir Caracteres
# Peça ao usuário uma string e um caractere para substituir, além do caractere novo.

palavra = input('informe a string: ').lower()
caracter_1 = input('informe o carctere para ser substituido: ').lower()
caracter_2 = input('informe o caracter para substituir: ')

palavra_substituida = palavra.replace(caracter_1,caracter_2)
print(palavra_substituida)