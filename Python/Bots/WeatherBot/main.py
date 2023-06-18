import telebot
import requests
import json

bot = telebot.TeleBot('6094002155:AAHQjy6cbku_f_SQWlVXwF_MywExfNAJewY')
API = 'cac929763b48c58bc8265bed8ffea50d'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Привет, сейчас тебя видеть! Введите название города')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    temperature = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if temperature.status_code == 200:
        data = json.loads(temperature.text)
        temp = data["main"]["temp"]
        image = 'sun.png' if temp > 15.0 else 'cold.png'
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
        bot.reply_to(message, f'Сейчас погода: {temp}. Введите новый город')
        bot.register_next_step_handler(message, get_weather)
    else:
        bot.reply_to(message, f'Город указан не верно')


bot.infinity_polling()
