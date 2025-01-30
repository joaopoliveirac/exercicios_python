# 3. Verificação de CPF Válido
# Peça ao usuário um CPF (somente números) e valide se ele é um CPF verdadeiro com base no cálculo dos dígitos verificadores.

# Exemplo:
# Entrada: "52998224725"
# Saída: "CPF válido" ou "CPF inválido"

def validar_cpf(cpf):
    # Verificar se o CPF tem 11 caracteres numéricos
    if len(cpf) != 11 or not cpf.isdigit():
        return 'CPF inválido'

    # Calculando o primeiro dígito verificador (dígito 10)
    cpf_int = [int(digit) for digit in cpf[:9]]  # Pega os 9 primeiros dígitos
    soma_1 = sum([cpf_int[i] * (10 - i) for i in range(9)])  # Multiplicação para o primeiro dígito
    digito_10 = (soma_1 * 10) % 11
    if digito_10 == 10:
        digito_10 = 0  # Se o resto for 10, o dígito é 0

    # Calculando o segundo dígito verificador (dígito 11)
    cpf_int.append(digito_10)  # Adiciona o primeiro dígito verificador à lista
    soma_2 = sum([cpf_int[i] * (11 - i) for i in range(10)])  # Multiplicação para o segundo dígito
    digito_11 = (soma_2 * 10) % 11
    if digito_11 == 10:
        digito_11 = 0  # Se o resto for 10, o dígito é 0

    # Verificando se os dígitos calculados são iguais aos fornecidos
    if int(cpf[9]) == digito_10 and int(cpf[10]) == digito_11:
        return 'CPF válido'
    else:
        return 'CPF inválido'

# Teste da função
cpf = input('Digite o CPF (somente números): ')
print(validar_cpf(cpf))
