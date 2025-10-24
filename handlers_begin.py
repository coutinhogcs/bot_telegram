from bot_instance import bot

@bot.message_handler(commands=['start'])
def opcao1(mensagem):
   texto = f"""Olá {mensagem.chat.first_name}, seja bem-vindo ao Bot de Vagas de Emprego em Tecnologia!

Aqui você encontrará as melhores oportunidades de trabalho na área de tecnologia.

Digite qualquer mensagem para ver as opções disponíveis.

   """
   bot.reply_to(mensagem, texto)