from bot_instance import bot

@bot.message_handler(commands=['Gupy_Backend'])
def Gupy(mensagem):
  texto = """Aqui estão os links com as melhores vagas de backend na Gupy:

https://portal.gupy.io/job-search/term=Backend&workplaceTypes[]=remote

  """
  bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=['Linkedin_Backend'])
def Gupy(mensagem):
  texto = """Aqui estão os links com as melhores vagas de backend na Linkedin:

https://www.linkedin.com/jobs/search/?currentJobId=4317203399&f_E=3%2C4&f_TPR=r86400&f_WT=2&geoId=106057199&keywords=Desenvolvedor%20de%20back%20end&origin=JOB_SEARCH_PAGE_KEYWORD_AUTOCOMPLETE&refresh=true

  """
  bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=['InfoJobs_Backend'])
def Gupy(mensagem):
  texto = """Aqui estão os links com as melhores vagas de backend na InfoJobs:

https://www.infojobs.com.br/vagas-de-emprego-programador+backend-trabalho-home-office.aspx

  """
  bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=['Catho_Backend'])
def Gupy(mensagem):
  texto = """Aqui estão os links com as melhores vagas de backend na Catho:

https://www.catho.com.br/vagas/desenvolvedor-back-end/?contract_type_id%5B0%5D=2&contract_type_id%5B1%5D=6&work_model%5B0%5D=remote&work_model%5B1%5D=hybrid&lastDays=15

  """
  bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=['Indeed_Backend'])
def Gupy(mensagem):
  texto = """Aqui estão os links com as melhores vagas de backend na Indeed:

https://br.indeed.com/jobs?q=desenvolvedor+back+end&l=&fromage=14&sc=0kf%3Aattr%28DSQF7%29%3B&from=searchOnDesktopSerp&vjk=fc4df3b88d56e269

  """
  bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=['Glassdoor_Backend'])
def Gupy(mensagem):
  texto = """Aqui estão os links com as melhores vagas de backend na Glassdoor:

https://www.glassdoor.com.br/Vaga/rio-de-janeiro-backend-developer-vagas-SRCH_IL.0,14_IC2402386_KO15,32.htm?remoteWorkType=1

  """
  bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=['Programathor_Backend'])
def Gupy(mensagem):
  texto = """Aqui estão os links com as melhores vagas de backend na Programathor:

Java:
https://programathor.com.br/jobs-java/remoto

Python:
https://programathor.com.br/jobs-python/remoto

C#:
https://programathor.com.br/jobs-c-sharp/remoto

#GO:
https://programathor.com.br/jobs-go/remoto

  """
  bot.send_message(mensagem.chat.id, texto)
