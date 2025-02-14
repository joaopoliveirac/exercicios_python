# 5-Classe JobScheduler para simular agendamento de tarefas
# Implemente uma classe Job
# Scheduler onde você pode adicionar tarefas com tempos de execução específicos, e ela executa as tarefas automaticamente no tempo correto.

from apscheduler.schedulers.background import BackgroundScheduler
import time

class JobScheduler:
    def __init__(self):
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()

    def adicionar_tarefa(self, tarefa, tempo_execucao, *args, **kwargs):
        """Adiciona uma tarefa a ser executada em um tempo específico"""
        self.scheduler.add_job(tarefa, 'date', run_date=tempo_execucao, args=args, kwargs=kwargs)
        print(f"Tarefa agendada para: {tempo_execucao}")
    
    def adicionar_tarefa_intervalo(self, tarefa, intervalo, *args, **kwargs):
        """Adiciona uma tarefa a ser executada com intervalo específico"""
        self.scheduler.add_job(tarefa, 'interval', seconds=intervalo, args=args, kwargs=kwargs)
        print(f"Tarefa agendada para rodar a cada {intervalo} segundos.")
    
    def parar_scheduler(self):
        """Parar o agendador"""
        self.scheduler.shutdown()
        print("Scheduler parado.")

# Exemplo de funções para tarefas agendadas
def minha_tarefa(nome):
    print(f"Tarefa executada! Olá, {nome}")

def tarefa_periodica():
    print("Tarefa periódica executada!")

if __name__ == "__main__":
    # Cria um agendador de tarefas
    scheduler = JobScheduler()

    # Agendando uma tarefa para ser executada em 5 segundos
    scheduler.adicionar_tarefa(minha_tarefa, time.time() + 5, "João")

    # Agendando uma tarefa para rodar a cada 3 segundos
    scheduler.adicionar_tarefa_intervalo(tarefa_periodica, 3)
    
    # Manter o script rodando para o agendador continuar a execução
    try:
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        scheduler.parar_scheduler()
