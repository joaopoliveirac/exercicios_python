# 5. Verificar se um Elemento Está na Lista
# Peça ao usuário um nome e verifique se ele está na lista: nomes = ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo']

nomes = ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo']
nome = input('Informe o nome a ser verificado na lista: ')

if nome.capitalize() in nomes:
    print(f'{nome} está na nossa lista de nomes.')
else:
    print('não ta na nossa lista :(')