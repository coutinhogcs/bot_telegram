import telebot 
# Importe as bibliotecas novas
from flask import Flask
from threading import Thread
import os # Importe 'os' para pegar a porta


API_TOKEN = os.environ.get('TELEGRAM_TOKEN') 
bot = telebot.TeleBot(API_TOKEN)
# --- CÓDIGO DO FLASK (O "SITE FALSO") ---
app = Flask(__name__)

# Esta é a página inicial do "site"
# O Render vai verificar se isso aqui funciona
@app.route('/')
def home():
    return "Olá! Eu sou um bot e estou vivo."

# Função para rodar o site
def run_flask():
    # Pega a porta que o Render nos dá. Se não achar, usa 8080.
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

# --- FIM DO CÓDIGO DO FLASK ---
# BOAS VINDAS
@bot.message_handler(commands=['start'])
def opcao1(mensagem):
   texto = f"""Olá {mensagem.chat.first_name} seja bem-vindo ao Bot de Vagas de Emprego em Tecnologia!
Aqui você encontrará as melhores oportunidades de trabalho na área de tecnologia.
Digite qualquer mensagem para ver as opções disponíveis.
   """
   bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['Gupy'])
def Gupy(mensagem):
  texto = """Aqui estão os links com as melhores vagas de frontend na Gupy:

https://portal.gupy.io/job-search/term=Frontend
  """
  bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=['Linkedin'])
def Gupy(mensagem):
  texto = """Aqui estão os links com as melhores vagas de frontend na Linkedin:

https://www.linkedin.com/jobs/search/?currentJobId=4316797240&f_E=3%2C4&f_TPR=r86400&f_WT=2&geoId=106057199&keywords=Desenvolvedor%20de%20front-end&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true
  """
  bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=['InfoJobs'])
def Gupy(mensagem):
  texto = """Aqui estão os links com as melhores vagas de frontend na InfoJobs:

https://www.infojobs.com.br/vagas-de-emprego-programador+front+end-em-rio-janeiro-trabalho-home-office.aspx
  """
  bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=['Catho'])
def Gupy(mensagem):
  texto = """Aqui estão os links com as melhores vagas de frontend na Catho:

https://www.catho.com.br/vagas/desenvolvedor-front-end/?contract_type_id%5B0%5D=2&contract_type_id%5B1%5D=6&work_model%5B0%5D=hybrid&work_model%5B1%5D=remote&lastDays=15
  """
  bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=['Indeed'])
def Gupy(mensagem):
  texto = """Aqui estão os links com as melhores vagas de frontend na Indeed:

https://br.indeed.com/jobs?q=desenvolvedor+front+end&l=Rio+de+Janeiro%2C+RJ&fromage=14&radius=100&from=searchOnDesktopSerp&vjk=5db5966fad94153b
  """
  bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=['Glassdoor'])
def Gupy(mensagem):
  texto = """Aqui estão os links com as melhores vagas de frontend na Glassdoor:

https://www.glassdoor.com.br/Vaga/rio-de-janeiro-front-end-vagas-SRCH_IL.0,14_IC2402386_KO15,24.htm?fromAge=14&minRating=3.0
  """
  bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=['Programathor'])
def Gupy(mensagem):
  texto = """Aqui estão os links com as melhores vagas de frontend na Programathor:

https://programathor.com.br/jobs-front-end/remoto
  """
  bot.send_message(mensagem.chat.id, texto)


# OPÇÕES DE VAGAS DISPONÍVEIS
@bot.message_handler(commands=['opcao1'])
def opcao1(mensagem):
   texto = """Opções de site para vagas FrontEnd:

/Gupy

/Linkedin

/InfoJobs

/Catho

/Indeed

/Glassdoor

/Programathor

"""
   bot.reply_to(mensagem, texto)




@bot.message_handler(commands=['opcao2'])
def opcao2(mensagem):
   texto = """Aqui estão os links com as melhores vagas de BackEnd:
https://portal.gupy.io/job-search/term=Backend&workplaceTypes[]=remote
   """
   bot.reply_to(mensagem, texto)


@bot.message_handler(commands=['opcao3'])
def opcao3(mensagem):
   texto = """Aqui estão os links com as melhores vagas de FullStack:
https://portal.gupy.io/job-search/term=Fullstack&workplaceTypes[]=remote
   """
   bot.reply_to(mensagem, texto)


@bot.message_handler(commands=['opcao4'])
def opcao4(mensagem):
   texto = """Aqui estão os links com as melhores vagas de Mobile:
https://portal.gupy.io/job-search/term=Mobile&workplaceTypes[]=remote
   """
   bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['opcao5'])
def opcao5(mensagem):
   texto = """Aqui estão os links com as melhores vagas de Data Science:
https://portal.gupy.io/job-search/term=Data%20Science&workplaceTypes[]=remote
   """ 
   bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['opcao6'])
def opcao6(mensagem):
   texto = """Aqui estão os links com as melhores vagas de DevOps:
https://portal.gupy.io/job-search/term=DevOps&workplaceTypes[]=remote
   """ 
   bot.reply_to(mensagem, texto) 

@bot.message_handler(commands=['opcao7'])
def opcao7(mensagem):
   texto = """Aqui estão os links com as melhores vagas de Analista de Banco de Dados:
https://portal.gupy.io/job-search/term=Analista%20de%20Banco%20de%20Dados&workplaceTypes[]=remote,on-site,hybrid
   """   
   bot.reply_to(mensagem, texto)

def verificar(mensagem):
   return True

# MENU PRINCIPAL
@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar:
    
/opcao1 Vagas de FrontEnd

/opcao2 Vagas de BackEnd

/opcao3 Vagas de FullStack

/opcao4 Vagas de Mobile

/opcao5 Vagas de Data Science

/opcao6 Vagas de DevOps

/opcao7 Vagas de Analista de Banco de Dados

clique para selecionar uma opção.
    """
    bot.reply_to(mensagem, texto)



# --- SEU CÓDIGO DO BOT ---
def seu_bot_principal():
    print("Iniciando o bot do Telegram...")
    bot.polling()

# --- FIM DO CÓDIGO DO BOT ---


# --- INICIALIZAÇÃO ---
if __name__ == "__main__":
    # 1. Cria uma "thread" para o site falso
    flask_thread = Thread(target=run_flask)
    
    # 2. Inicia o site falso
    flask_thread.start()
    
    # 3. Inicia o seu bot na "thread" principal
    seu_bot_principal()




