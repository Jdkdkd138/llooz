import os
import threading
import traceback
from flask import Flask
import bot_handlers

app = Flask(__name__)

@app.route('/')
def home():
    return "OK", 200

@app.route('/health')
def health():
    return "OK", 200

def run_bot():
    try:
        print("🚀 BOT POLLING STARTED", flush=True)
        bot_handlers.bot.polling(non_stop=True, timeout=35, long_polling_timeout=25)
    except Exception as e:
        print(f"💥 BOT CRASHED: {e}", flush=True)
        traceback.print_exc()
        threading.Timer(10, run_bot).start()

if __name__ == '__main__':
    print("🔥 STARTING BOT THREAD", flush=True)
    threading.Thread(target=run_bot, daemon=True).start()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
