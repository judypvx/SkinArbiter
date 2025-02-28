import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Загружаем .env
load_dotenv(dotenv_path="bot/config/.env")

MONGO_URI = os.getenv("MONGO_URI", "mongodb://root:example@mongodb:27017/?authSource=admin")
client = MongoClient(MONGO_URI)
db = client["skin_arbiter_db"]

def test_connection():
    print("Список коллекций:", db.list_collection_names())
