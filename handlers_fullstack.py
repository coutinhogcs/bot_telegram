from bot_instance import bot

@bot.message_handler(commands=['Gupy_FullStack'])
def Gupy(mensagem):
  texto = """Aqui estão os links com as melhores vagas de fullstack na Gupy:

https://portal.gupy.io/job-search/term=FullStack&workplaceTypes[]=remote
  """
  bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=['Linkedin_FullStack'])
def Gupy(mensagem):
  texto = """Aqui estão os links com as melhores vagas de fullstack na Linkedin:

https://www.linkedin.com/jobs/search/?currentJobId=4317203399&f_E=3%2C4&f_TPR=r86400&f_WT=2&geoId=106057199&keywords=Desenvolvedor%20full%20stack&origin=JOB_SEARCH_PAGE_KEYWORD_AUTOCOMPLETE&refresh=true
  """
  bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=['InfoJobs_FullStack'])
def Gupy(mensagem):
  texto = """Aqui estão os links com as melhores vagas de fullstack na InfoJobs:

https://www.infojobs.com.br/vagas.aspx?palabra=programador+fullstack&provincia=182
  """
  bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=['Catho_FullStack'])
def Gupy(mensagem):
  texto = """Aqui estão os links com as melhores vagas de fullstack na Catho:

https://www.catho.com.br/vagas/desenvolvedor-full-stack/?contract_type_id%5B0%5D=2&contract_type_id%5B1%5D=6&work_model%5B0%5D=remote&work_model%5B1%5D=hybrid&lastDays=15
  """
  bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=['Indeed_FullStack'])
def Gupy(mensagem):
  texto = """Aqui estão os links com as melhores vagas de fullstack na Indeed:

https://br.indeed.com/jobs?q=desenvolvedor+full+stack&l=&fromage=14&sc=0kf%3Aattr%28DSQF7%29%3B&from=searchOnDesktopSerp&vjk=5b1fcbc35a19d23e
  """
  bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=['Glassdoor_FullStack'])
def Gupy(mensagem):
  texto = """Aqui estão os links com as melhores vagas de fullstack na Glassdoor:

  https://www.glassdoor.com.br/Vaga/rio-de-janeiro-full-stack-developer-vagas-SRCH_IL.0,14_IC2402386_KO15,35.htm?remoteWorkType=1
  
  """
  bot.send_message(mensagem.chat.id, texto)


# @bot.message_handler(commands=['Programathor_FullStack'])
# def Gupy(mensagem):
#   texto = """Aqui estão os links com as melhores vagas de fullstack na Programathor:

# https://programathor.com.br/jobs-front-end/remoto
#   """
#   bot.send_message(mensagem.chat.id, texto)
