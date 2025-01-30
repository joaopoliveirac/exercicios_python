# 9. Verificar Login e Senha
# Crie um sistema que peça um nome de usuário e senha. Caso estejam corretos, exiba "Login bem-sucedido", caso contrário, "Usuário ou senha incorretos."

def verificar_usuario(usuario_banco,senha_banco,usuario_digitado,senha_digitada):
    if usuario_banco == usuario_digitado and senha_banco == senha_digitada:
        return True
    else:
        return False
    
usuario_banco = 'admin'
senha_banco = '12345'

usuario_digitado = input('informe o usuario: ')
senha_digitada = input('informe a senha: ')

if verificar_usuario(usuario_banco,senha_banco,usuario_digitado,senha_digitada):
    print('entoru')
else:
    print('alguma coisa errada.')

