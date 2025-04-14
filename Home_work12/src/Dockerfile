# Используем официальный образ Python 3.9
FROM python:3.9-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код приложения
COPY . .

# Открываем порт 8000
EXPOSE 8000

# Запускаем gunicorn с нашим API на порту 8000, привязанном к 0.0.0.0
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
