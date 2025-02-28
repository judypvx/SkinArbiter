import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv


# Загружаем переменные окружения из .env
load_dotenv(dotenv_path="config/.env")

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN не найден в переменных окружения!")

# Инициализируем бота и диспетчер
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Привет! Я готов к работе.")

async def main():
    # Запуск бота с помощью asyncio
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
