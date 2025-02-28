# Базовый образ Python 3.10
FROM python:3.10-slim

# Рабочая директория внутри контейнера
WORKDIR /app

# Копируем и устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Запускаем бота (предположим, что main.py лежит в bot/db)
CMD ["python", "bot/main.py"]
