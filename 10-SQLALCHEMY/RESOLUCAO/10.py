# 10. Trabalhando com Data e Hora
# Crie uma classe Evento com os campos id, nome, data_inicio e data_fim. 
# Insira alguns eventos e faça uma consulta para encontrar todos os eventos que começam após uma data específica.


from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime
from conexao_postgre import ConexaoBD

Base = declarative_base()

class Evento(Base):
    __tablename__ = 'eventos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    data_inicio = Column(DateTime)
    data_fim = Column(DateTime)

db = ConexaoBD("postgres", "1234", "localhost", "5432", "exercicio_10")
Base.metadata.create_all(db.engine)

sessao = db.conectar()

# Inserindo eventos com datas variadas
eventos = [
    Evento(nome='Lançamento de Produto', data_inicio=datetime(2025, 3, 15, 14, 0), data_fim=datetime(2025, 3, 15, 18, 0)),
    Evento(nome='Treinamento SQL', data_inicio=datetime(2025, 4, 10, 9, 0), data_fim=datetime(2025, 4, 10, 17, 0)),
    Evento(nome='Hackathon', data_inicio=datetime(2025, 5, 20, 8, 0), data_fim=datetime(2025, 5, 22, 20, 0)),
    Evento(nome='Palestra sobre IA', data_inicio=datetime(2025, 2, 5, 19, 0), data_fim=datetime(2025, 2, 5, 21, 0)),
    Evento(nome='Meetup Python', data_inicio=datetime(2025, 6, 1, 18, 0), data_fim=datetime(2025, 6, 1, 22, 0))
]

sessao.add_all(eventos)
sessao.commit()

# Data de referência para a consulta
data_referencia = datetime(2025, 4, 1, 0, 0)

# Consulta para encontrar eventos que começam após a data especificada
consulta = sessao.query(Evento).filter(Evento.data_inicio > data_referencia).all()

print(f"Eventos que começam após {data_referencia}:")
for evento in consulta:
    print(f"Nome: {evento.nome}, Início: {evento.data_inicio}, Fim: {evento.data_fim}")
