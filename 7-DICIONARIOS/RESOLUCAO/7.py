# 7. Iterar sobre um Dicionário
# Crie um dicionário com nomes de países como chaves e suas populações como valores. Exiba todos os países e suas populações.

paises = {'brasil' : 4565465, 'frança': 454545465, 'japao' : 546465449898 , 'eua': 787798}
for pais,populacao in paises.items():
    print(f'{pais} tem {populacao} habitantes.')