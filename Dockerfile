# Используйте официальный образ Python
FROM python:3.12.3

# Установите рабочую директорию
WORKDIR /app

# Скопируйте файлы с зависимостями
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Скопируйте исходный код
COPY app.py app.py

# Укажите команду для запуска приложения
CMD ["python", "app.py"]
