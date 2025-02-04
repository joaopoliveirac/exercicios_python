# 10. Mesclar Dois Dicionários
# Dado dois dicionários, mescle-os em um único dicionário.

dicionario_01 = {'joao': 25, 'jose': 23}
dicionario_02 = {'carlin': 37, 'renata': 55}
dicionario_03 = dicionario_01 | dicionario_02
print(dicionario_03)