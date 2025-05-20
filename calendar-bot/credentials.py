import os
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()

SCOPES = [
    "https://www.googleapis.com/auth/calendar.readonly",
    "https://www.googleapis.com/auth/tasks.readonly"
]

def carregar_credenciais():
    creds = None
    token_path = 'token.pickle'
    client_secret_file = os.getenv("GOOGLE_CLIENT_SECRET", "credentials_oauth.json")

    if os.path.exists(token_path):
        with open(token_path, 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                client_secret_file, SCOPES
            )
            # Evita erro com redirect_uri, porta pode ser a 9090 (confirme no console Google Cloud)
            creds = flow.run_local_server(port=9090, redirect_uri_trailing_slash=True)

        with open(token_path, 'wb') as token:
            pickle.dump(creds, token)

    service_calendar = build("calendar", "v3", credentials=creds)
    service_tasks = build("tasks", "v1", credentials=creds)
    return service_calendar, service_tasks
