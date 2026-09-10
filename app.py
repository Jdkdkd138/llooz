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
    while True:
        try:
            print("🚀 BOT POLLING STARTED", flush=True)
            bot_handlers.bot.polling(non_stop=True, timeout=35, long_polling_timeout=25)
        except Exception as e:
            print(f"💥 BOT CRASHED: {e}", flush=True)
            traceback.print_exc()
            print("🔁 RESTARTING IN 5 SECONDS...", flush=True)
            import time
            time.sleep(5)

if __name__ == '__main__':
    print("🔥 STARTING BOT THREAD", flush=True)
    threading.Thread(target=run_bot, daemon=True).start()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
