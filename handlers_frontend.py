from bot_instance import bot

@bot.message_handler(commands=['Gupy_Frontend'])
def Gupy(mensagem):
  texto = """Aqui estão os links com as melhores vagas de frontend na Gupy:

https://portal.gupy.io/job-search/term=Frontend
  """
  bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=['Linkedin_Frontend'])
def Gupy(mensagem):
  texto = """Aqui estão os links com as melhores vagas de frontend na Linkedin:

https://www.linkedin.com/jobs/search/?currentJobId=4316797240&f_E=3%2C4&f_TPR=r86400&f_WT=2&geoId=106057199&keywords=Desenvolvedor%20de%20front-end&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true
  """
  bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=['InfoJobs_Frontend'])
def Gupy(mensagem):
  texto = """Aqui estão os links com as melhores vagas de frontend na InfoJobs:

https://www.infojobs.com.br/vagas-de-emprego-programador+front+end-em-rio-janeiro-trabalho-home-office.aspx
  """
  bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=['Catho_Frontend'])
def Gupy(mensagem):
  texto = """Aqui estão os links com as melhores vagas de frontend na Catho:

https://www.catho.com.br/vagas/desenvolvedor-front-end/?contract_type_id%5B0%5D=2&contract_type_id%5B1%5D=6&work_model%5B0%5D=hybrid&work_model%5B1%5D=remote&lastDays=15
  """
  bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=['Indeed_Frontend'])
def Gupy(mensagem):
  texto = """Aqui estão os links com as melhores vagas de frontend na Indeed:

https://br.indeed.com/jobs?q=desenvolvedor+front+end&l=Rio+de+Janeiro%2C+RJ&fromage=14&radius=100&from=searchOnDesktopSerp&vjk=5db5966fad94153b
  """
  bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=['Glassdoor_Frontend'])
def Gupy(mensagem):
  texto = """Aqui estão os links com as melhores vagas de frontend na Glassdoor:

https://www.glassdoor.com.br/Vaga/rio-de-janeiro-front-end-vagas-SRCH_IL.0,14_IC2402386_KO15,24.htm?fromAge=14&minRating=3.0
  """
  bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=['Programathor_Frontend'])
def Gupy(mensagem):
  texto = """Aqui estão os links com as melhores vagas de frontend na Programathor:

https://programathor.com.br/jobs-front-end/remoto
  """
  bot.send_message(mensagem.chat.id, texto)
