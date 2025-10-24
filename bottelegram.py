import telebot 
from flask import Flask
from threading import Thread
from bot_instance import bot
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Olá! Eu sou um bot e estou vivo."

def run_flask():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

@bot.message_handler(commands=['start'])
def opcao1(mensagem):
   texto = f"""Olá {mensagem.chat.first_name} seja bem-vindo ao Bot de Vagas de Emprego em Tecnologia!
Aqui você encontrará as melhores oportunidades de trabalho na área de tecnologia.
Digite qualquer mensagem para ver as opções disponíveis.
   """
   bot.reply_to(mensagem, texto)



def seu_bot_principal():
    print("Iniciando o bot do Telegram...")
    bot.polling()



if __name__ == "__main__":
    flask_thread = Thread(target=run_flask)
    
    flask_thread.start()
    
    seu_bot_principal()




