import os
import requests
from utils import log
from dotenv import load_dotenv

load_dotenv()

session = 'NERDWHATS_AMERICA'
WHATSAPP_NUMBER = os.getenv("WHATSAPP_NUMBER")
WPP_API_URL = os.getenv("WPP_API_URL")
WPP_API_SECRETKEY = os.getenv("WPP_API_SECRETKEY")

def enviar_mensagem(mensagem):
    try:
        url = f'{WPP_API_URL}/api/{session}/send-message'
        headers = {'Authorization': f'Bearer {WPP_API_SECRETKEY}'}
        payload = {'phone': WHATSAPP_NUMBER, 'message': mensagem}
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            log("✅ Mensagem enviada com sucesso!")
        else:
            log(f"❌ Erro ao enviar mensagem: {response.text}")
    except Exception as e:
        log(f"Erro ao enviar mensagem: {e}")
