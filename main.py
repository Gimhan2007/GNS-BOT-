  import os
  import telebot

  bot =telebot.TeleBot("API Key Here")

@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message,"Hello! Iam Gimhan Geek Chat Bot")

@bot.message_handler(commands="how")
def send_message(message):
  bot.send_message(message, "https://youtube.com/c/GimhanGeek")

bot.polling()
