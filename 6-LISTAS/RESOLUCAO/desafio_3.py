# 3. Criar um Sistema de Pontuação
# Crie um programa que armazene a pontuação de jogadores em uma lista e exiba:

def armazenar_pontuacao():
    pontuacao_total = []
    while True:
        nome = input('informe o nome do jogador ou sair para parar. ')
        if nome.lower() == 'sair':
            break
        else:
            pontuacao = input('Informe a pontuacao desse jogador.')
            pontuacao_total.append([nome,pontuacao])
    for nome,pontuacao in pontuacao_total:
        print(f'{nome} tem {pontuacao}')

armazenar_pontuacao()

