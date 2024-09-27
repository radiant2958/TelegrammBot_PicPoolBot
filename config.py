import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

API_TOKEN = os.getenv('API_TOKEN')  # Токен бота из .env файла
if not API_TOKEN:
    raise ValueError("Не удалось загрузить API_TOKEN из .env файла.")

DESTINATION_CHAT_ID = os.getenv('DESTINATION_CHAT_ID')
if DESTINATION_CHAT_ID is None:
    raise ValueError("Не удалось загрузить DESTINATION_CHAT_ID из .env файла.")
try:
    DESTINATION_CHAT_ID = int(DESTINATION_CHAT_ID)
except ValueError:
    raise ValueError(f"DESTINATION_CHAT_ID должен быть числом. Получено: {DESTINATION_CHAT_ID}")