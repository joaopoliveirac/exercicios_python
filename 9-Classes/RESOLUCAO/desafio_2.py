# 2-Classe Pipeline para processamento de dados
# Implemente uma classe Pipeline que recebe funções e as executa em sequência sobre um conjunto de dados. Exemplo:
# pipeline = Pipeline([limpar_dados, normalizar, salvar_csv])
# pipeline.executar(dados)
import pandas as pd

class Pipeline:
    def __init__(self,arquivo):
        self.arquivo = arquivo
        self.df = None

    def carregar(self):
        self.df = pd.read_csv(self.arquivo)
        if self.df is not None:
            return 'ARQUIVO CARREGADO COM SUCESSO'
        else:
            return 'NENHUM ARQUIVO CARREGADO'
    
    def tratar_dados(self,agrupamento):
        self.df = self.df.groupby(agrupamento, as_index=False).sum(numeric_only=True)
        return self.df
    
    def carregar_arquivo(self,nome):
        self.df.to_csv(nome, index=False)
        return f'Arquivo {nome} salvo com sucesso.'

pipeline = Pipeline('tips.csv')
print(pipeline.carregar())
print(pipeline.tratar_dados('sex'))
print(pipeline.carregar_arquivo('tips_agrupado_1.csv'))

    

        


