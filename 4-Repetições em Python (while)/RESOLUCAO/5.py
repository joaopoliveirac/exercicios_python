# 5. Verificação de Senha
# Crie um sistema que continue pedindo uma senha até que o usuário digite "1234".

def verificar_senha():
    senha = '1234'
    senha_usuario = str(input('informe a senha: '))
    while senha != senha_usuario:
        print('Senha incorreta.')
        senha_usuario = str(input('informe a senha: '))
    return 'Senha correta.'

print(verificar_senha())