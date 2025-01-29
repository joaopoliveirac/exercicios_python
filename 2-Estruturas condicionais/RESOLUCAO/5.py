# 5. Verificar Idade para Carteira de Motorista
# Peça a idade do usuário e informe se ele pode tirar a carteira de motorista (idade ≥ 18).


def verificar_idade_carteira(idade):
    if idade >= 18:
        print('Voce pode tirar a carteira.')
    else:
        print('não está na hora, aguarde os 18 anos')

idade = int(input('informe a sua idade:'))

verificar_idade_carteira(idade)