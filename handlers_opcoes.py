from bot_instance import bot

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
