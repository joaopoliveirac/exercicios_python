# 4. Jogo do Pedra, Papel e Tesoura
# Crie um jogo em que o usuário joga contra o computador (escolha aleatória entre "pedra", "papel" ou "tesoura").

# Exemplo:
# Entrada: "pedra"
# Computador escolheu: "tesoura"
# Saída: "Você venceu!"

import random

def jogo(opcoes,escolha):
    valor_aleatorio = random.choice(opcoes)
    if escolha == valor_aleatorio:
        return f'maquina: {valor_aleatorio}, voce: {escolha} EMPATE'
    if escolha == 'pedra' and valor_aleatorio == 'tesoura':
        return f'maquina: {valor_aleatorio}, voce: {escolha} VOCE VENCEU'
    elif escolha == 'tesoura' and valor_aleatorio == 'papel':
        return f'maquina: {valor_aleatorio}, voce: {escolha} VOCE VENCEU'
    elif escolha == 'papel' and valor_aleatorio == 'pedra':
        return f'maquina: {valor_aleatorio}, voce: {escolha} VOCE VENCEU'
    else:
        return f'maquina: {valor_aleatorio}, voce: {escolha} VOCE PERDEU PRA MAQUINA!'

opcoes = ['pedra', 'papel', 'tesoura']
escolha = input('informe pedra, papel ou tesoura: ').lower()
print(jogo(opcoes,escolha))



#resposta do GPTECO, aqui ele realmente deixou o código mais simples
def jogo(opcoes, escolha):
    valor_aleatorio = random.choice(opcoes)
    if escolha == valor_aleatorio:
        return f'Máquina: {valor_aleatorio}, Você: {escolha} EMPATE'
    
    if (escolha == 'pedra' and valor_aleatorio == 'tesoura') or \
       (escolha == 'tesoura' and valor_aleatorio == 'papel') or \
       (escolha == 'papel' and valor_aleatorio == 'pedra'):
        return f'Máquina: {valor_aleatorio}, Você: {escolha} VOCÊ VENCEU!'
    else:
        return f'Máquina: {valor_aleatorio}, Você: {escolha} VOCÊ PERDEU PRA MÁQUINA!'

opcoes = ['pedra', 'papel', 'tesoura']
escolha = input('Informe pedra, papel ou tesoura: ').lower()
print(jogo(opcoes, escolha))
