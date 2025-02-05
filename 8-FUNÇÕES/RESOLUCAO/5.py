# 5. Função com Lista de Parâmetros
# Crie uma função media(lista) que recebe uma lista de números e retorna a média desses números.

def media(lista):
    return sum(lista)/len(lista)

lista = [10,50,60]
print(media(lista))