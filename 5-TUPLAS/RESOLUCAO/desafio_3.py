# 3. Verificar Anagrama com Tuplas
# Peça ao usuário duas palavras e verifique se são anagramas usando tuplas.

# Exemplo:
# Entrada: "amor", "roma"
# Saída: "São anagramas!"

palavra_01 = input('primeira palavra: ')
palavra_02 = input('segunda palavra')
lista = []
lista.extend((palavra_01,palavra_02))
tupla = tuple(lista)
print(tupla)
if sorted(tupla[0]) == sorted(tupla[1]):
    print('são anagramas.')