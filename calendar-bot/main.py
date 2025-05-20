import time
import schedule
from credentials import carregar_credenciais
from calendar_events import carregar_eventos
from calendar_tasks import carregar_tarefas
from mensagem import enviar_mensagem
from utils import log

def tarefa_diaria():
    log("⏰ Executando tarefa diária...")
    service_calendar, service_tasks = carregar_credenciais()
    eventos_texto = carregar_eventos(service_calendar)
    tarefas_texto = carregar_tarefas(service_tasks)
    mensagem = eventos_texto + "\n" + tarefas_texto
    log(mensagem)
    enviar_mensagem(mensagem)

if __name__ == "__main__":
    schedule.every().day.at("17:17").do(tarefa_diaria)
    log("🚀 Bot iniciado e aguardando o horário programado...")
    while True:
        schedule.run_pending()
        time.sleep(30)
