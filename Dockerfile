# Используем базовый образ Python
FROM python:3.12.3

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы зависимостей
COPY requirements.txt requirements.txt

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем приложение
COPY app.py app.py

# Запускаем Gunicorn (или uWSGI)
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000"]
