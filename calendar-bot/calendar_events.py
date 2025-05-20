from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
from utils import log

load_dotenv()
CALENDAR_ID = os.getenv("CALENDAR_ID")

def carregar_eventos(service_calendar):
    mensagens = []
    try:
        agora = datetime.utcnow()
        inicio_do_dia = agora.replace(hour=0, minute=0, second=0, microsecond=0)
        fim_do_dia = agora.replace(hour=23, minute=59, second=59, microsecond=999999)

        eventos_resultado = service_calendar.events().list(
            calendarId=CALENDAR_ID,
            timeMin=inicio_do_dia.isoformat() + 'Z',
            timeMax=fim_do_dia.isoformat() + 'Z',
            singleEvents=True,
            orderBy="startTime"
        ).execute()

        eventos = eventos_resultado.get('items', [])
        if eventos:
            mensagens.append("📆 *Eventos de hoje:*")
            for evento in eventos:
                inicio = evento['start'].get('dateTime', evento['start'].get('date'))
                titulo = evento.get('summary', 'Sem título')
                mensagens.append(f"🕒 {inicio} - {titulo}")
        else:
            mensagens.append("📭 Hoje você não tem eventos agendados.")
    except Exception as e:
        log(f"Erro ao carregar eventos: {e}")
        mensagens.append("❌ Erro ao carregar eventos.")
    return "\n".join(mensagens)
