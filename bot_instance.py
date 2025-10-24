import os
import telebot  

API_TOKEN = os.environ.get('TELEGRAM_TOKEN') 
bot = telebot.TeleBot(API_TOKEN)