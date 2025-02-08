# 6-Classe Aluno com métodos estáticos
# Crie uma classe Aluno com nome e notas (uma lista). Adicione um método estático media(notas) para calcular a média das notas.

#Métodos estáticos são usados quando a função não precisa acessar self, ou seja, não depende de atributos da instância.

class Aluno:
    def __init__(self, nome,notas):
        self.nome = nome
        self.notas = list(notas)

    @staticmethod
    def media(notas):
        media = sum(notas) / len(notas)
        return media

aluno_01 = Aluno('Joao', [5,7,9,10])
print(f'{aluno_01.nome} teve uma media de {Aluno.media(aluno_01.notas)} na escola.')
#agora a funcao media (metodo) que eu criei pode ser usada sem criar um objeto (aluno_01). ex:
lista_notas = [9,9,8,8]
print(Aluno.media(lista_notas))
    