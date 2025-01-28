# 4. Verificar se é um Palíndromo
# Crie um programa que verifica se uma palavra é um palíndromo (lida da mesma forma de trás para frente).

palavra = input('informe a palavra a ser analisada: ').lower()

if palavra[:] == palavra[::-1]:
    print('Essa palavra é um palíndromo.')
else:
    print('Não é um palíndromo.')