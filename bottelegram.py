from flask import Flask
from threading import Thread
from bot_instance import bot
import os
import time
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


# --- AQUI ESTÁ A MUDANÇA ---
def seu_bot_principal():
    print("Iniciando o bot do Telegram...")
    
    while True: # <-- 2. Adiciona um loop infinito
        try:
            # 3. Tenta rodar o polling (non_stop=True é uma boa prática)
            bot.polling(non_stop=True, interval=0) 
        
        except Exception as e:
            # 4. Se der QUALQUER erro (ConnectionError, etc.)
            print(f"Erro no polling: {e}")
            print("Reiniciando o bot em 5 segundos...")
            time.sleep(5) # 5. Espera 5 segundos antes de tentar de novo



if __name__ == "__main__":
    flask_thread = Thread(target=run_flask)
    
    flask_thread.start()
    
    seu_bot_principal()




