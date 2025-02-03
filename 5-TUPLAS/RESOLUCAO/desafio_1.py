# 1. Encontrar Elementos Únicos
# Dada uma tupla com números repetidos, crie uma nova tupla apenas com os elementos únicos.

# Exemplo:
# Entrada: (1, 2, 2, 3, 4, 4, 5, 5, 5)
# Saída: (1, 2, 3, 4, 5)

tupla_geral = (1, 2, 2, 3, 4, 4, 5, 5, 5)
set_unicos = set(tupla_geral)
tupla_unico = tuple(set_unicos)
print(tupla_unico)

