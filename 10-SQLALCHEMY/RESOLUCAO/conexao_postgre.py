from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

class ConexaoBD:
    def __init__(self, usuario, senha, host, porta, banco):
        """String de conexão com o PostgreSQL"""
        if senha:
            self.database_url = f"postgresql://{usuario}:{senha}@{host}:{porta}/{banco}"
        else:
            self.database_url = f"postgresql://{usuario}@{host}:{porta}/{banco}"
        
        self.engine = create_engine(self.database_url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def conectar(self):
        """Cria uma sessão de conexão com o banco"""
        try:
            session = self.SessionLocal()
            return session
        except SQLAlchemyError as e:
            print(f"Erro ao conectar: {e}")
            return None

    def fechar_conexao(self, session):
        """Fecha a sessão do banco"""
        if session:
            session.close()
