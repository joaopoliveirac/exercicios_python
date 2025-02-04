# 1. Filtrar Números Pares e Ímpares
# Crie uma lista com 10 números e separe-os em duas listas: uma com os pares e outra com os ímpares.

lista = [1,2,3,4,5,6,7,8,9,10]
lista_pares = [numero for numero in lista if numero % 2 == 0]
lista_impares = [numero for numero in lista if numero % 2 != 0]
print(f'Nossa lista de numeros pares: {lista_pares}. \n Nossa lista de numeros ímpares{lista_impares}.')