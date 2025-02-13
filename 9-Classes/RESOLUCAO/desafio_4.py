# 4-Classe ConexaoBD para interação com PostgreSQL
# Desenvolva uma classe ConexaoBD que se conecta a um banco de dados PostgreSQL, executa consultas SQL e retorna os resultados.

from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

class ConexaoBD:
    def __init__(self, usuario, senha, host, porta, banco):
        """Cria a string de conexão com o PostgreSQL"""
        if senha:
            self.database_url = f"postgresql://{usuario}:{senha}@{host}:{porta}/{banco}"
        else:
            self.database_url = f"postgresql://{usuario}@{host}:{porta}/{banco}"
        
        self.engine = None  # Inicializa sem conexão ativa

    def conectar(self):
        """Cria a engine de conexão com o banco"""
        try:
            self.engine = create_engine(self.database_url)
            return "Conexão estabelecida com sucesso."
        except SQLAlchemyError as e:
            return f"Erro ao conectar ao banco de dados: {e}"

    def executar_consulta(self, consulta, parametros=None):
        """Executa uma consulta SQL e retorna os resultados"""
        if self.engine is None:
            return "Erro: conexão não estabelecida."

        try:
            with self.engine.connect() as conexao:
                resultado = conexao.execute(text(consulta), parametros or {})
                
                if resultado.returns_rows:
                    return resultado.fetchall()  # Retorna os resultados se houver
                
                return "Consulta executada com sucesso."
        except SQLAlchemyError as e:
            return f"Erro ao executar a consulta: {e}"

    def fechar_conexao(self):
        """Fecha a conexão com o banco"""
        if self.engine:
            self.engine.dispose()
            return "Conexão fechada com sucesso."

if __name__ == "__main__":
    db = ConexaoBD("postgres", "nova_senha", "localhost", "5432", "partition")
    print(db.conectar())

    consulta = "SELECT * FROM pessoas where id = 1"
    resultados = db.executar_consulta(consulta, {'id': 1})
    print(resultados)

    print(db.fechar_conexao())

    

