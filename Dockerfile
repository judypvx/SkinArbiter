# Используем официальный образ Python 3.10 slim
FROM python:3.10-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл зависимостей и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в контейнер
COPY . .

# Запускаем бота; путь должен соответствовать расположению main.py
CMD ["python", "-m", "bot.main"]
