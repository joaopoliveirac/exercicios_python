# 4. Contar Vogais em uma Palavra
# Peça ao usuário uma palavra e conte quantas vogais (a, e, i, o, u) existem nela.

vogais = ['a', 'e', 'i', 'o', 'u']
palavra = input('informe uma palavra').lower()
quantidade = 0

for vogal in vogais:
    for caracter in palavra:
        if vogal in caracter:
            quantidade += 1

print(quantidade)



 #esse foi do gpteco, contador ficou mais simplificado do que um for dentro de outro for.
def contar_vogais(palavra):
    vogais = "aeiouAEIOU"
    contador = sum(1 for letra in palavra if letra in vogais)
    return contador

palavra = input("Digite uma palavra: ")
print(f"A palavra '{palavra}' tem {contar_vogais(palavra)} vogal(is).")