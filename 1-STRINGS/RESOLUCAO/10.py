# 10. Substituir Vogais por *
# Crie um programa que substitua todas as vogais de uma string pelo caractere *.

frase = input('informe a frase: ')
vogais = ['a', 'e', 'i', 'o', 'u']

for vogal in vogais:
    if vogal in frase:
        frase = frase.replace(vogal,'*')

print(frase)