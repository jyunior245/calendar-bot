from utils import log

def carregar_tarefas(service_tasks):
    mensagens = []
    try:
        tarefas_resultado = service_tasks.tasks().list(tasklist='@default').execute()
        tarefas = tarefas_resultado.get('items', [])

        if tarefas:
            mensagens.append("\n✅ *Tarefas de hoje:*")
            for tarefa in tarefas:
                titulo = tarefa.get('title', 'Sem título')
                mensagens.append(f"📌 {titulo}")
        else:
            mensagens.append("📭 Você não tem tarefas para hoje.")
    except Exception as e:
        log(f"Erro ao buscar tarefas: {e}")
        mensagens.append("❌ Ocorreu um erro ao buscar as tarefas.")
    return "\n".join(mensagens)
