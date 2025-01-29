# 3. Expressões Regulares - Encontrar Endereços de E-mail
# Use a biblioteca re para identificar e extrair endereços de e-mail de um texto.

import re
texto = 'joaopolalal@gmail.com é o meu email, o email do jose é josefino@hotmail.com'
emails = re.findall(r"\S+@\S+",texto) #\S+ Captura caracteres que não são espaço antes e depois de @
print(', '.join(emails))
