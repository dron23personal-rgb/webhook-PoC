from fastapi import FastAPI, Request
import logging
import sys
from pythonjsonlogger import jsonlogger

app = FastAPI()

logger = logging.getLogger()
logger.setLevel(logging.INFO)  # будем записывать всё от INFO и выше

json_formatter = jsonlogger.JsonFormatter(
    fmt='%(asctime)s %(levelname)s %(name)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

console_formatter = logging.Formatter(
    fmt='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

file_handler = logging.FileHandler('app.log.json')
file_handler.setFormatter(json_formatter)
logger.addHandler(file_handler)

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    logging.info(f"Получен вебхук: {data}")
    return {"status": "ok"}
