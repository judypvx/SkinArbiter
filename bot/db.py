import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

client = MongoClient(MONGO_URI)
db = client["skin_arbiter_db"]  # Название базы

# Пример тестовой функции
def test_connection():
    print("Список коллекций в базе:", db.list_collection_names())
