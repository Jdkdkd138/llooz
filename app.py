import os
import threading
from flask import Flask
import bot_handlers

app = Flask(__name__)

# ✅ Отвечаем на любые запросы (чтобы UptimeRobot и другие могли нас найти)
@app.route('/')
def home():
    return "OK", 200

@app.route('/health')
def health():
    return "OK", 200

def run_bot():
    try:
        bot_handlers.bot.polling(non_stop=True, timeout=35, long_polling_timeout=25)
    except Exception as e:
        print(f"Bot polling crashed: {e}")
        # Создаём новый поток, чтобы бот не умер навсегда
        threading.Timer(10, run_bot).start()

if __name__ == '__main__':
    threading.Thread(target=run_bot, daemon=True).start()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
