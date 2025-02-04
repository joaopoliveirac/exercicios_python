# 5. Criar uma Tabela com Tuplas
# Crie um programa que armazena os dados de 5 produtos em uma tupla contendo: (nome, preço, quantidade). Depois, exiba uma tabela formatada com os dados.


produtos = (
    ('notebook', 3000, 10),
    ('computador', 4000, 5),
    ('tenis', 500, 6))

for nome,preco, quantide in produtos:
    print(nome)
    print(preco)
    print(quantide)