import telebot
from telebot import types
import requests
from datetime import datetime, timedelta
import flask

bot = telebot.TeleBot('6759330550:AAH_4Po0L6qb3MvrSGhX9K-2Ph_C5FPIKOw')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    usr = message.from_user.first_name
    text = f"Welcome, [{usr}](tg://settings)! 🤖\n\n_🎉🤖 Welcome to BARD AI Bot! 🌟🚀_\n\n_Hey there, fellow humanoids! 🤗 I'm the party starter, the chat sensation, the one and only BARD AI Bot! 🎩💬_\n\n_I'm equipped with wit, humor, and an arsenal of emojis! 🤓✨ Let's chat and sprinkle some sparkles of fun all around! 🌈✨_\n\n_Whether it's a joke, a story, or just a friendly chat, I'm here for it! 📚🗨️\nSo, how's your day going? Tell me everything! 🌞🌸_"
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    developer_button = types.InlineKeyboardButton(text='💸 SANCHIT 💸', url='https://t.me/X668F')
    ista = types.InlineKeyboardButton(text='🔮 Follow Me On Instagram 🔮', url='https://www.instagram.com/sanch1t')
    keyboard.add(developer_button,ista)
    bot.reply_to(message, text, parse_mode='markdown', reply_markup=keyboard)
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_sticker(message.chat.id, "CAACAgEAAxkBAAIHtWWK_7zf8Yst4vAC2KQyXbqQ1JCcAAIpBAACCW5ZRFmkpjp2avNlMwQ")
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id, f"Hey, This Is [Bard Ai](tg://settings).\nHow Can I Help You [{usr}](tg://settings) ?", parse_mode='markdown')

@bot.message_handler(func=lambda message: True)
def reply_to_user(message):
    uid = message.from_user.id
    un = message.from_user.first_name
    wait_msg = bot.reply_to(message, "_Please wait for a few seconds..._ ⏳🥺", parse_mode='markdown')
    text = message.text
    res = chatbot(uid, text)
    bot.delete_message(message.chat.id, wait_msg.message_id)
    bot.send_chat_action(message.chat.id, 'typing')
    bot.reply_to(message, f"_{res}_", parse_mode="Markdown")

def chatbot(uid, text):
    url = requests.get(f"https://api.safone.dev/bard?message={text}").json()    
    res = url['candidates'][0]['content']['parts'][0]['text']
    return res


bot.infinity_polling()
