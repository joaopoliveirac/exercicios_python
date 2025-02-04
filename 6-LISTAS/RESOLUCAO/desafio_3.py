# 3. Criar um Sistema de Pontuação
# Crie um programa que armazene a pontuação de jogadores em uma lista e exiba:

# O maior e menor pontuação
# A média das pontuações

def armazenar_pontuacao():
    pontuacao_total = []
    while True:
        nome = input('informe o nome do jogador ou sair para parar. ')
        if nome.lower() == 'sair':
            break
        else:
            pontuacao = int(input('Informe a pontuacao desse jogador.'))
            pontuacao_total.append([nome,pontuacao])
    for nome,pontuacao in pontuacao_total:
        print(f'{nome} tem {pontuacao}')
    pontuacao = [pontos[1] for pontos in pontuacao_total]
    maior_pontuacao = max(pontuacao_total, key=lambda x: x[1])
    menor_pontuacao = min(pontuacao_total, key=lambda x: x[1])
    media = sum(pontuacao) / len(pontuacao)
    return maior_pontuacao,menor_pontuacao,media

print(armazenar_pontuacao())

