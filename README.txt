# Запуск (proof-of-concept)

# После скачивания репозитория установить зависимости
pip install -r requirements.txt

# Запустить сервер:
uvicorn main:app --reload

# Используя curl, отправить тестовый POST-запрос c JSON на http://127.0.0.1:8000/webhook
curl.exe -X POST http://127.0.0.1:8000/webhook -H "Content-Type: application/json" -d '{\"message\":\"Привет, бот!\", \"chat_id\": 123}'

# Логи будут выведены в консоль, а также файл app.log.json