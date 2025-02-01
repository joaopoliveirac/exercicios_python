# 2. Contagem de Palavras em um Texto
# Peça ao usuário uma frase e conte quantas palavras existem nela (considerando espaços como separadores).

# Exemplo:
# Entrada: "Eu gosto de programar em Python"
# Saída: 6 palavras

def contar_palavras(texto):
    palavras = texto.split()
    return f"{len(palavras)}"

print(contar_palavras('joao pedro oliveira'))