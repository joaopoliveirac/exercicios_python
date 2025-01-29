# 4. Aprovação de Nota
# Peça ao usuário a nota de um aluno (de 0 a 10) e informe se ele foi aprovado (nota ≥ 7), em recuperação (5 ≤ nota < 7) ou reprovado (nota < 5).


def aprovacao(nota):
    if nota >= 7:
        print('aprovado.')
    elif 5 <= nota < 7:
        print('recuperacao')
    else:
        print('reprovado.')

nota = float(input('informe a nota: '))
aprovacao(nota)