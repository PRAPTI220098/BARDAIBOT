import os 
import telebot
from telebot import types
import requests
from datetime import datetime, timedelta
import flask
from user_agent import generate_user_agent as rrr
bot = telebot.TeleBot('6643702223:AAGf-EKPO5Z4LzyAplYgEaE2yb86X3J0Qac')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    usr = message.from_user.first_name
    text = f"Welcome, [{usr}](tg://settings)! 🤖\n\n_🎉🤖 Welcome to BARD AI Bot! 🌟🚀_\n\n_Hey there, fellow humanoids! 🤗 I'm the party starter, the chat sensation, the one and only BARD AI Bot! 🎩💬_\n\n_I'm equipped with wit, humor, and an arsenal of emojis! 🤓✨ Let's chat and sprinkle some sparkles of fun all around! 🌈✨_\n\n_Whether it's a joke, a story, or just a friendly chat, I'm here for it! 📚🗨️\nSo, how's your day going? Tell me everything! 🌞🌸_"
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    developer_button = types.InlineKeyboardButton(text='💸 SANCHIT 💸', url='https://t.me/X668F')
    ista = types.InlineKeyboardButton(text='🔮 Follow Me On Instagram 🔮', url='https://www.instagram.com/sanch1t')
    keyboard.add(developer_button,ista)
    bot.reply_to(message, text, parse_mode='markdown', reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def reply_to_user(message):
    uid = message.from_user.id
    un = message.from_user.first_name
    wait_msg = bot.send_message(message.chat.id, "<i>🔍 Searching On It...</i>", parse_mode='HTML')
    text = message.text
    res = chatbot(message, uid, text)
    bot.edit_message_text(f"{res}", message.chat.id, wait_msg.message_id, parse_mode='Markdown')

def chatbot(message, uid, text):
  head = {
    'Host': 'api.safone.dev',
    'user-agent': str(rrr())
  }
  url = requests.get(f"https://api.safone.dev/bard?message={text}", headers=head).json()
  try:
  	res = url['candidates'][0]['content']['parts'][0]['text']
  	return res
  except:
  	bot.send_message(message.chat.id,f"_Regrettably, your choice of words includes prohibited language. Kindly opt for more suitable expressions. 🚫🗣️ Let's keep the conversation positive!_ 🌟👍",parse_mode='Markdown')	

bot.infinity_polling()
