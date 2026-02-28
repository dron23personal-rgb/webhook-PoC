from fastapi import FastAPI, Request
import logging
import sys
from pythonjsonlogger import jsonlogger

# Создаём экземпляр FastAPI
app = FastAPI()

# Настраиваем корневой логгер (главный объект для логирования)
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # будем записывать всё от INFO и выше

# Форматтер для JSON-логов (для файла)
# Включаем временную метку, уровень, имя логгера и сообщение
json_formatter = jsonlogger.JsonFormatter(
    fmt='%(asctime)s %(levelname)s %(name)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Форматтер для консоли (человекочитаемый текст)
console_formatter = logging.Formatter(
    fmt='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Обработчик для записи в файл (в формате JSON)
file_handler = logging.FileHandler('app.log.json')
file_handler.setFormatter(json_formatter)
logger.addHandler(file_handler)

# Обработчик для вывода в консоль (в текстовом формате)
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)

@app.post("/webhook")
async def webhook(request: Request):
    # Извлекаем JSON из тела запроса
    data = await request.json()
    # Логируем полученные данные (они попадут и в файл, и в консоль)
    logging.info(f"Получен вебхук: {data}")
    # Отвечаем клиенту, что всё принято
    return {"status": "ok"}