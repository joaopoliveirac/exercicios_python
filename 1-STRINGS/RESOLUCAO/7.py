# 7. Primeira Letra Maiúscula
# Peça ao usuário para digitar uma frase e retorne a mesma frase com a primeira letra de cada palavra em maiúscula.

frase = input('digite uma frase: ').lower()
frase_1 = frase.split()
lista_correta = []
qtde = 0

while qtde < len(frase_1):
    lista = frase_1[qtde]
    palavra_convertida = lista.replace(lista[0], lista[0].upper())
    lista_correta.append(palavra_convertida)
    qtde += 1

print(' '.join(lista_correta))


frase = input("Digite uma frase: ")
# Converte para título (primeira letra de cada palavra maiúscula)
#problema do método title é que ele só consegue separar se for por espaço, caso as palavras não estejam separadas por espaços ele nao roda.
frase_formatada = frase.title()

print("Frase formatada:", frase_formatada)




