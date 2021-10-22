import telebot

from config import TOKEN_MANAGER

bot = telebot.TeleBot(TOKEN_MANAGER)

def send_order(text_order):
    bot.send_message(850731060, text_order, parse_mode='html')
