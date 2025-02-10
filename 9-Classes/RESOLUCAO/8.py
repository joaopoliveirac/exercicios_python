# 8-Classe Sensor e manipulação de arquivos
# Implemente uma classe Sensor que lê dados de um arquivo CSV e retorna a média dos valores de uma determinada coluna.

import pandas as pd

class Sensor:
    def __init__(self, arquivo):
        self.arquivo = arquivo
    
    def ler_arquivo(self):
        return pd.read_csv(self.arquivo)
    
    def calcular_media(self):
        df = self.ler_arquivo()
        media = df['media'].mean()
        return media

sensor = Sensor('dados.csv')
print(sensor.calcular_media())
        
        