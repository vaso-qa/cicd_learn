# Используем образ Python
FROM python:3.12.3

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы
COPY requirements.txt requirements.txt
COPY app.py app.py
COPY test_app.py test_app.py

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Указываем команду запуска
CMD ["python", "app.py"]
