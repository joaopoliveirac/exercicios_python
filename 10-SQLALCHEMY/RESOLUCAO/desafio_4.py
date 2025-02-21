# Crie uma tabela Veiculo com os campos id e modelo, e duas classes filhas Carro e Moto, cada uma com atributos adicionais específicos. 
# Use herança de classes no SQLAlchemy para mapear essas classes para uma única tabela (tabela única de herança).

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import ForeignKey
from conexao_postgre import ConexaoBD

Base = declarative_base()

# Tabela base: Veiculo
class Veiculo(Base):
    __tablename__ = 'veiculos'
    id = Column(Integer, primary_key=True)
    modelo = Column(String(50))
    tipo = Column(String(50))  # Tipo de veículo (Carro ou Moto)

    __mapper_args__ = {
        'polymorphic_identity': 'veiculo',
        'polymorphic_on': tipo
    }

# Tabela derivada: Carro
class Carro(Veiculo):
    numero_portas = Column(Integer)

    __mapper_args__ = {
        'polymorphic_identity': 'carro',
    }

# Tabela derivada: Moto
class Moto(Veiculo):
    tipo_guidom = Column(String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'moto',
    }

# Configuração do banco
db = ConexaoBD("postgres", "1234", "localhost", "5432", "desafio_4")
Base.metadata.create_all(db.engine)

sessao = db.conectar()

# Inserindo dados
veiculos = [
    Carro(modelo='Fusca', numero_portas=4),
    Carro(modelo='Civic', numero_portas=4),
    Moto(modelo='Titan', tipo_guidom='Esportivo'),
    Moto(modelo='CB500', tipo_guidom='Naked')
]

sessao.add_all(veiculos)
sessao.commit()

# Consulta para listar todos os veículos
todos_veiculos = sessao.query(Veiculo).all()

print("Todos os veículos registrados:")
for veiculo in todos_veiculos:
    if isinstance(veiculo, Carro):
        print(f"Carro: {veiculo.modelo}, Número de portas: {veiculo.numero_portas}")
    elif isinstance(veiculo, Moto):
        print(f"Moto: {veiculo.modelo}, Tipo de guidão: {veiculo.tipo_guidom}")

