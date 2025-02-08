# 5-Classe Livro e método especial __str__
# Crie uma classe Livro com titulo, autor e ano. 
# Sobrescreva o método __str__ para exibir a informação de maneira amigável.

class Livro:
    def __init__(self,titulo,autor,ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
    
    def __str__(self):
        return f'O livro {self.titulo} do autor {self.autor} foi publicado em {self.ano}'
    


livro_01 = Livro('joao macarena', 'josefino', 1999)
print(livro_01)