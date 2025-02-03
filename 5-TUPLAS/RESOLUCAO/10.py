# 10. Criar uma Tupla a Partir de uma Lista
# Peça ao usuário uma lista de números separados por espaço e converta-a para uma tupla.

lista_usuario = input('informe uma lista de numeros, separada por espaços: ')
lista = lista_usuario.split()
tupla = tuple(lista)
print(tupla)