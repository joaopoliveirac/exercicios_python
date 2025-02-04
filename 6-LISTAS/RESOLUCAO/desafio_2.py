# 2. Remover Elementos Duplicados
# Dada uma lista com elementos repetidos, crie uma nova lista sem duplicatas.
# Exemplo:
# Entrada: [1, 2, 3, 2, 4, 5, 5, 6]
# Saída: [1, 2, 3, 4, 5, 6]

lista = [1,1,1,3,6,9,3,3,5,4,4,8,7,7,6,3,1]
lista_sem_duplicados = set(lista)
lista_sem_duplicados = list(lista_sem_duplicados)
print(lista_sem_duplicados)