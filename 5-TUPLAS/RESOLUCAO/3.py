# 3. Verificar se um Elemento Está na Tupla
# Peça ao usuário um nome e verifique se ele está na tupla:

tupla = ('joao','pedro','oliveira','carvalho')
nome = str(input('informe um nome: '))
if nome in tupla:
    print(f'{nome} está na nossa tupla.')