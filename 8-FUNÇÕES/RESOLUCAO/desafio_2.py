# 2. Função que Verifica Palíndromos
# Crie uma função verifica_palindromo(s) que recebe uma string s e 
# retorna True se a string for um palíndromo (ou seja, pode ser lida da mesma forma de trás para frente), e False caso contrário.

def verificar_palíndromos(s):
    if s == s[::-1]:
        return True
    else:
        return False
    
print(verificar_palíndromos('radar'))