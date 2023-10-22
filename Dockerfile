# пулим образ питона
FROM python:3.11-slim
# устанавливаем рабочую директорию внутри контейнера
WORKDIR /vapefeed/
# копируем requirements в корень рабочей директории
COPY requirements.txt .
# устанавливаем необходимые пакеты из скопированного requerements
RUN pip install --no-cache-dir -r requirements.txt
# ???
COPY . .
# Запускаем команду запуска asgi сервера и нашего приложения с хостом и портом
CMD ["uvicorn", "users.main:app", "--host", "0.0.0.0", "--port", "8000"]