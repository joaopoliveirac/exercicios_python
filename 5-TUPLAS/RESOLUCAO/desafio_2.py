# 2. Jogo de Estatísticas com Tuplas
# Peça ao usuário para digitar 10 números e armazene-os em uma tupla. Depois, exiba:

# A média dos números
# Quantos são pares
# Quantos são ímpares

lista = []
for i in range(1,11):
    numero = int(input('informe um numero'))
    lista.append(numero)
tupla = tuple(lista)
media = sum(tupla) / len(tupla)
pares = (numero for numero in tupla if numero % 2 == 0)
impares = (numero for numero in tupla if numero % 2 != 0)
print(media)
print(tuple(pares))
print(tuple(impares))