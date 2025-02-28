import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Загружаем переменные окружения
# Если рабочая директория при запуске — корень проекта, указываем путь относительно него
load_dotenv(dotenv_path="bot/config/.env")

MONGO_URI = os.getenv("MONGO_URI", "mongodb://root:example@mongodb:27017/?authSource=admin")
client = MongoClient(MONGO_URI)
db = client["skin_arbiter_db"]

def test_connection():
    """Выводит список коллекций для проверки подключения к MongoDB."""
    collections = db.list_collection_names()
    print("Коллекции в базе:", collections)
