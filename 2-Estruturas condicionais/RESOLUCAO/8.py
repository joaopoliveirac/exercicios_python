# 8. Ano Bissexto
# Peça ao usuário um ano e informe se ele é bissexto ou não.

def eh_bissexto(ano):
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        return True
    return False

# Testando com alguns anos
anos = [2024, 1900, 2000, 2100, 2400]
for ano in anos:
    if eh_bissexto(ano):
        print(f"{ano} é bissexto.")
    else:
        print(f"{ano} não é bissexto.")
