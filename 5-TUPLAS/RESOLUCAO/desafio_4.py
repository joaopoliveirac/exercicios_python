# 4. Criar uma Tupla de Palavras Ordenadas
# Peça ao usuário uma frase e armazene cada palavra em uma tupla ordenada alfabeticamente.

# Exemplo:
# Entrada: "Python é uma linguagem poderosa"
# Saída: ('Python', 'é', 'linguagem', 'poderosa', 'uma')

texto = input('digite um texto a ser ordenado: ')
lista = []
lista.extend(texto.split())
tupla = tuple(lista)
print(sorted(tupla))
