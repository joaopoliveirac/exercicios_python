# 2. Acessar Elementos da Tupla
# Dada a tupla meses = ('Janeiro', 'Fevereiro', 'Março', ..., 'Dezembro'), peça ao usuário um número de 1 a 12 e exiba o mês correspondente.

meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
numero_mes = int(input('informe o numero do mes: '))
print(f'O numero {numero_mes} corresponde ao mes {meses[numero_mes - 1]}')
