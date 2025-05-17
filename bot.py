import telebot

TOKEN = "7524886478:AAF4MkQzjDMqMIKiYgj43-pWGUPXK2caj9g"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Assalomu alaykum! Men sarmoya botman. Sizga qanday yordam bera olaman?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
