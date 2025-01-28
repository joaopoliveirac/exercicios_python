# 6. Juntar e Separar Palavras
# Crie um programa que peça uma frase ao usuário e a divida em palavras, depois junte novamente usando um hífen (-).

frase = input('Informe uma frase: ')
palavras = frase.split()
frase_hifen = '-'.join(palavras)
print(f'{palavras} \n {frase_hifen}')