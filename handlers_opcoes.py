from bot_instance import bot

@bot.message_handler(commands=['opcao1'])
def opcao1(mensagem):
   texto = """Opções de site para vagas FrontEnd:

/Gupy_Frontend

/Linkedin_Frontend

/InfoJobs_Frontend

/Catho_Frontend

/Indeed_Frontend

/Glassdoor_Frontend

/Programathor_Frontend

"""
   bot.reply_to(mensagem, texto)




@bot.message_handler(commands=['opcao2'])
def opcao2(mensagem):
   texto = """Opções de site para vagas BackEnd:

/Gupy_Backend

/Linkedin_Backend

/InfoJobs_Backend

/Catho_Backend

/Indeed_Backend

/Glassdoor_Backend

/Programathor_Backend

"""
   bot.reply_to(mensagem, texto)


@bot.message_handler(commands=['opcao3'])
def opcao3(mensagem):
   texto = """Opções de site para vagas FullStack:

/Gupy_FullStack

/Linkedin_FullStack

/InfoJobs_FullStack

/Catho_FullStack

/Indeed_FullStack

/Glassdoor_FullStack

"""
   bot.reply_to(mensagem, texto)


@bot.message_handler(commands=['opcao4'])
def opcao4(mensagem):
   texto = """Opções de site para vagas Mobile:

/Gupy_Mobile

/Linkedin_Mobile

/InfoJobs_Mobile

/Catho_Mobile

/Indeed_Mobile

/Glassdoor_Mobile

/Programathor_Mobile

"""
   bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['opcao5'])
def opcao5(mensagem):
   texto = """Opções de site para vagas Data Science:

/Gupy_Data_Science

/Linkedin_Data_Science

/InfoJobs_Data_Science

/Catho_Data_Science

/Indeed_Data_Science

/Glassdoor_Data_Science

/Programathor_Data_Science

""" 
   bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['opcao6'])
def opcao6(mensagem):
   texto = """Opções de site para vagas DevOps:

/Gupy_DevOps

/Linkedin_DevOps


/InfoJobs_DevOps


/Catho_DevOps


/Indeed_DevOps


/Glassdoor_DevOps


/Programathor_DevOps


""" 
   bot.reply_to(mensagem, texto) 

@bot.message_handler(commands=['opcao7'])
def opcao7(mensagem):
   texto = """Opções de site para vagas Analista de Banco de Dados:

/Gupy_BD

/Linkedin_BD

/InfoJobs_BD

/Catho_BD

/Indeed_BD

/Glassdoor_BD

/Programathor_BD

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
