# Crie uma tabela Vendas com os campos id, data_venda, produto e valor. 
# Calcule o valor acumulado das vendas para cada produto ao longo do tempo usando funções de janela (ex: row_number(), sum() over()) e aliases.

from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date

Base = declarative_base()

# Tabela Vendas
class Venda(Base):
    __tablename__ = 'vendas'
    id = Column(Integer, primary_key=True)
    data_venda = Column(Date)
    produto = Column(String(50))
    valor = Column(Float)

# Configuração do banco de dados
DATABASE_URL = "postgresql://postgres:1234@localhost:5432/desafio_5"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
sessao = Session()

# Inserindo dados na tabela Vendas
vendas = [
    Venda(data_venda=date(2025, 1, 1), produto='Produto A', valor=100),
    Venda(data_venda=date(2025, 1, 2), produto='Produto A', valor=150),
    Venda(data_venda=date(2025, 1, 3), produto='Produto B', valor=200),
    Venda(data_venda=date(2025, 1, 4), produto='Produto A', valor=50),
    Venda(data_venda=date(2025, 1, 5), produto='Produto B', valor=250),
]

sessao.add_all(vendas)
sessao.commit()

# Consultando o valor acumulado de vendas por produto ao longo do tempo
from sqlalchemy import select

# Função de janela para calcular o valor acumulado
subquery = (
    select([
        Venda.produto,
        Venda.data_venda,
        Venda.valor,
        func.sum(Venda.valor).over(
            partition_by=Venda.produto,  # Agrupar por produto
            order_by=Venda.data_venda  # Ordenar por data de venda
        ).label('valor_acumulado')
    ])
    .order_by(Venda.produto, Venda.data_venda)  # Ordenando os resultados
).alias('vendas_acumuladas')  # Criar alias para a subconsulta

# Realizando a consulta
resultados = sessao.execute(select(subquery)).fetchall()  # Corrigido aqui

# Exibindo os resultados
print("Valor acumulado de vendas por produto ao longo do tempo:")
for row in resultados:
    print(f"Produto: {row.produto}, Data da Venda: {row.data_venda}, "
          f"Valor da Venda: {row.valor}, Valor Acumulado: {row.valor_acumulado}")

