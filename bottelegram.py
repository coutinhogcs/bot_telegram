from flask import Flask
from threading import Thread
from bot_instance import bot
import os
import handlers_begin
import handlers_frontend
import handlers_backend
import handlers_fullstack
import handlers_mobile
import handlers_data_science
import handlers_devops
import handlers_db
import handlers_opcoes

app = Flask(__name__)

@app.route('/')
def home():
    return "Olá! Eu sou um bot e estou vivo."

def run_flask():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)



def seu_bot_principal():
    print("Iniciando o bot do Telegram...")
    bot.polling()



if __name__ == "__main__":
    flask_thread = Thread(target=run_flask)
    
    flask_thread.start()
    
    seu_bot_principal()




