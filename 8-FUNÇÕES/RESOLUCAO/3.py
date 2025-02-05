# 3. Função com Condicional
# Crie uma função verifica_par_impar(n) que recebe um número n e retorna "Par" se o número for par e "Ímpar" se for ímpar.

def verificar_par_impar(n):
    if n % 2 == 0:
        return 'Par'
    else:
        return 'Impar'
    
print(verificar_par_impar(4))