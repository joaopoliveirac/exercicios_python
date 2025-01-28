# 3. Contar Ocorrências de uma Letra
# Escreva um programa que peça ao usuário uma palavra e uma letra. O programa deve contar quantas vezes a letra aparece na palavra.

palavra = input('informe uma palavra: ').lower()
letra = input('informe uma letra: ').lower()

print(palavra.count(letra))

