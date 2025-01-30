# 5. Classificador de Senhas
# Peça ao usuário uma senha e classifique seu nível de segurança:

# Fraca → Menos de 6 caracteres
# Média → De 6 a 10 caracteres
# Forte → Mais de 10 caracteres, contendo letras maiúsculas, minúsculas, números e símbolos
# Exemplo:
# Entrada: "Python123!"
# Saída: "Senha Forte"

import string

def verificao_senha(senha):
    lista= []
    if len(senha) < 6:
        return 'Senha fraca.'
    elif 6 <= len(senha) <= 10:
        return 'Senha Média.'
    else:
        maiuscula = any(char.isupper() for char in senha)
        minuscula = any(char.islower() for char in senha)
        numero = any(char.isdigit() for char in senha)
        simbolo = any(char in string.ponctuation for char in senha)

        if maiuscula and minuscula and numero and simbolo:
            return 'SENHA FORTE'
        else:
            return 'SENHA MEDIA'

senha = input('informe sua senha')
print(verificao_senha(senha))