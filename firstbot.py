import json
import telebot
from telebot import types
from telebot import apihelper
apihelper.ENABLE_MIDDLEWARE = True

bot = telebot.TeleBot('5332125448:AAEpFaZX2m4i1lVTXbiHb_658b3HflSo0sU')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name}</b>, \nсладкая ты моя <u>шоколадная</u> булочка☺'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands=['photo'])
def photo(message):
    mess = f'Кинь сюда какую-нибудь фотку, я заценю'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('👇🏻Нажми тут👇🏻', url='https://www.wildberries.ru/lk/myorders/delivery'))
    bot.send_message(message.chat.id,'Посмотри свои доставки на WB', reply_markup=markup)

@bot.message_handler(commands=['help'])
def help(message):
     helpMess=f'Если что-то не получается - напиши мне @ilonaleks и я помогу разобраться'
     bot.send_message(message.chat.id, helpMess, parse_mode='html')

@bot.message_handler(commands=['love'])
def love(message):
     LoveMess=f'😘😘😘 целую крепко-крепко ❤'
     bot.send_message(message.chat.id, LoveMess, parse_mode='html')
     LoveMess2=f'и обнимаю 🤗'
     bot.send_message(message.chat.id, LoveMess2, parse_mode='html', timeout=1000)

@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, "Вау, крутая фотка!😍")

@bot.message_handler(commands=['talks'])
def talks(message):
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
     Ukraine = types.KeyboardButton('Украина')
     Weather = types.KeyboardButton('Погода')
     Dreams = types.KeyboardButton('Сны')
     Plans = types.KeyboardButton('Планы')
     Shops  = types.KeyboardButton('Покупки')
     Capture = types.KeyboardButton('Хочешь смешную картинку?')
     markup.add(Ukraine, Weather, Dreams, Plans, Shops, Capture)
     bot.send_message(message.chat.id, 'Выбери тему', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def user_text(message):
    if message.text == "Украина":
        bot.send_message(message.chat.id, f"Я уверена на все 💯 - <b><i><u>ВОЙНА СКОРО ЗАКОНЧИТСЯ!!</u></i></b>", parse_mode='html')
    elif message.text == "Погода":
        bot.send_message(message.chat.id, "У природы нет плохой погоды", parse_mode='html')
    #     def big_weather(message, city):
    #         latitude, longitude = geo_pos(city)
    #         cod_loc = code_location(latitude, longitude, token_accu)
    #         you_weather = weather(cod_loc, token_accu)
    #         print_weather(you_weather, message)
    elif message.text == "Сны":
        bot.send_message(message.chat.id, f"Что бы тебе сегодня не приснилось - всё к лучшему!", parse_mode='html')
    elif message.text == "Планы":
        bot.send_message(message.chat.id, f"Какие планы на вечер?", parse_mode='html')
    elif message.text == "Покупки":
        bot.send_message(message.chat.id, f"На что опять спустила деньги?)))", parse_mode='html')
    else:
        capture = open('image_2022.png', "rb")
        bot.send_photo(message.chat.id, capture)

bot.infinity_polling(interval=0, timeout=20)
