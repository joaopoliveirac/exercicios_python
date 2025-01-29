# 2. Verificar se Duas Strings são Anagramas
# Crie uma função que recebe duas palavras e verifica se elas são anagramas (ou seja, possuem as mesmas letras, apenas reorganizadas).

def verificar_anagrama(str_01,str_02):
    if sorted(str_01) == sorted(str_02): 
        print('São anagramas')
    else:
        print('não são anagramas')

palavra_01 = input('informe a primeira string').lower()
palavra_02 = input('informe a segunda string').lower()
verificar_anagrama(palavra_01,palavra_02)





