import os 
import telebot
from telebot import types
import requests
import flask
from user_agent import generate_user_agent as rrr
bot = telebot.TeleBot('6643702223:AAFLg_zpxoxHD8QhhYw3IPUzedKzg8rK8QQ')
@bot.message_handler(commands=['start'])
def send_welcome(message):
    	usr = message.from_user.first_name
    	text = f"Welcome, [{usr}](tg://settings)! 🤖\n\n_🎉🤖 Welcome to BARD AI Bot! 🌟🚀_\n\n_Hey there, fellow humanoids! 🤗 I'm the party starter, the chat sensation, the one and only BARD AI Bot! 🎩💬_\n\n_I'm equipped with wit, humor, and an arsenal of emojis! 🤓✨ Let's chat and sprinkle some sparkles of fun all around! 🌈✨_\n\n_Whether it's a joke, a story, or just a friendly chat, I'm here for it! 📚🗨️\nSo, how's your day going? Tell me everything! 🌞🌸_"
    	keyboard = types.InlineKeyboardMarkup(row_width=1)
    	dev = types.InlineKeyboardButton(text='💸 SANCHIT 💸', url='https://t.me/X668F')
    	ista = types.InlineKeyboardButton(text='🔮 Follow Me On Instagram 🔮', url='https://www.instagram.com/sanch1t')
    	keyboard.add(dev, ista)
    	de=requests.get(f"https://translate-api-mu.vercel.app/translate?from=auto&to={message.from_user.language_code}&text={text}").json()['translation']
    	bot.reply_to(message, de, parse_mode='markdown', reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def reply_to_user(message):
    uid = message.from_user.id
    un = message.from_user.first_name
    wait_msg = bot.send_message(message.chat.id, "<i>🔍 Searching On It...</i>", parse_mode='HTML')
    text = message.text
    res = chatbot(message, uid, text)
    bot.edit_message_text(f"{res}", message.chat.id, wait_msg.message_id, parse_mode='Markdown')

def chatbot(message, uid, text):    
  tr = requests.get(f"https://translate-api-mu.vercel.app/translate?from=auto&to={message.from_user.language_code}&text={text}").json()['translation']
  url = requests.get(f"https://api.safone.dev/bard?message={tr}",headers={"accept": "application/json"}).json()
  try:  	
  	res = url['candidates'][0]['content']['parts'][0]['text']
  	return res
  except:
  	de=requests.get(f"https://translate-api-mu.vercel.app/translate?from=auto&to={message.from_user.language_code}&text=_Regrettably, your choice of words includes prohibited language. Kindly opt for more suitable expressions. 🚫🗣️ Let's keep the conversation positive!_ 🌟👍").json()['translation']
  	bot.send_message(message.chat.id, de,parse_mode='Markdown')	

server = flask.Flask(__name__)

@server.route("/bot", methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(flask.request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    link = 'https://'+str(flask.request.host)
    bot.set_webhook(url=f"{link}/bot")
    return "Success!", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=8080)
