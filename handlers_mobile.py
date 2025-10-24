from bot_instance import bot

@bot.message_handler(commands=['Gupy_Mobile'])
def Gupy(mensagem):
  texto = """Aqui estão os links com as melhores vagas de mobile na Gupy:

https://portal.gupy.io/job-search/term=Mobile&workplaceTypes[]=remote
 
   """
  bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=['Linkedin_Mobile'])
def Gupy(mensagem):
  texto = """Aqui estão os links com as melhores vagas de mobile na Linkedin:

https://www.linkedin.com/jobs/search/?currentJobId=4317203399&f_E=3%2C4&f_TPR=r86400&f_WT=2&geoId=106057199&keywords=Desenvolvedor%20de%20aplicativos%20móveis&origin=JOB_SEARCH_PAGE_KEYWORD_AUTOCOMPLETE&refresh=true
  
  """
  bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=['InfoJobs_Mobile'])
def Gupy(mensagem):
  texto = """Aqui estão os links com as melhores vagas de mobile na InfoJobs:

https://www.infojobs.com.br/vagas.aspx?palabra=programador+mobile
  
  """
  bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=['Catho_Mobile'])
def Gupy(mensagem):
  texto = """Aqui estão os links com as melhores vagas de mobile na Catho:

https://www.catho.com.br/vagas/desenvolvedor-mobile/?contract_type_id%5B0%5D=2&contract_type_id%5B1%5D=6&work_model%5B0%5D=remote&work_model%5B1%5D=hybrid&lastDays=15
  
  """
  bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=['Indeed_Mobile'])
def Gupy(mensagem):
  texto = """Aqui estão os links com as melhores vagas de mobile na Indeed:

https://br.indeed.com/jobs?q=desenvolvedor+mobile&l=&fromage=14&sc=0kf%3Aattr%28DSQF7%29%3B&from=searchOnDesktopSerp&vjk=20a81f7f2aa47150
  
  """
  bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=['Glassdoor_Mobile'])
def Gupy(mensagem):
  texto = """Aqui estão os links com as melhores vagas de mobile na Glassdoor:

https://www.glassdoor.com.br/Vaga/rio-de-janeiro-mobile-developer-vagas-SRCH_IL.0,14_IC2402386_KO15,31.htm?remoteWorkType=1
 
   """
  bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=['Programathor_Mobile'])
def Gupy(mensagem):
  texto = """Aqui estão os links com as melhores vagas de mobile na Programathor:

Android: 
https://programathor.com.br/jobs-android/remoto

iOS: 
https://programathor.com.br/jobs-ios/remoto

React Native:
https://programathor.com.br/jobs-react-native/remoto

  """
  bot.send_message(mensagem.chat.id, texto)
