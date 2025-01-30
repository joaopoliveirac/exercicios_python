# 2. Conversor de Notas para Conceito
# Peça ao usuário uma nota de 0 a 100 e converta para conceito:
# 90 a 100 → A
# 80 a 89 → B
# 70 a 79 → C
# 60 a 69 → D
# Menor que 60 → F
# Exemplo:
# Entrada: 85
# Saída: "Seu conceito é B"

def conversor_de_notas (nota):
    conceito = ['A', 'B', 'C', 'D', 'F']
    if nota < 0 or nota > 100:
        return 'Digite uma nota de 0 a 100'
    if 90 <= nota <= 100:
        nota_convertida = conceito[0]
    elif 80 <= nota < 89:
        nota_convertida = conceito[1]
    elif 70 <= nota < 79:
        nota_convertida = conceito[2]
    elif 60 <= nota < 69:
        nota_convertida = conceito[3]
    elif 60 > nota > 0:
        nota_convertida = conceito[4]
    return f'Seu conceito é {nota_convertida}'

nota = int(input('informe sua nota: '))
print(conversor_de_notas(nota))
        