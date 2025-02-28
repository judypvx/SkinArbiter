import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv

# Импортируем функции работы с БД
from bot.db.db import db, test_connection

load_dotenv(dotenv_path="bot/config/.env")
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
print("TOKEN:", TOKEN)  # Для отладки
if not TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN не найден в окружении!")


bot = Bot(token=TOKEN)
dp = Dispatcher()

# Команда /start
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Привет! Я работаю на aiogram 3.x")

# Команда /testdb для проверки подключения к MongoDB
@dp.message(Command("testdb"))
async def test_db_handler(message: types.Message):
    test_connection()  # Вывод в консоль списка коллекций
    users_collection = db["users"]
    result = users_collection.insert_one({
        "telegram_id": message.from_user.id,
        "name": message.from_user.first_name
    })
    await message.answer(
        f"Тест БД выполнен!\nСоздан документ с _id: {result.inserted_id}"
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
