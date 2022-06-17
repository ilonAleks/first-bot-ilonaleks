import json
import telebot
# import requests as req
# from os import environ
from telebot import types
from telebot import apihelper
# from geopy import geocoders
apihelper.ENABLE_MIDDLEWARE = True
#apihelper.proxy = {'http':'http://10.10.1.10:3128'}
#или вариант с socks5
# apihelper.proxy = {'https':'socks5://userproxy:password@proxy_address:port'}

bot = telebot.TeleBot('5332125448:AAEpFaZX2m4i1lVTXbiHb_658b3HflSo0sU')
# token_accu = environ['kaerAl70bhdlLqleLK0nHE08abqsdC27']
#
# def geo_pos(city: str):
#     geolocator = geocoders.Nominatim(user_agent="telebot")
#     latitude = str(geolocator.geocode(city).latitude)
#     longitude = str(geolocator.geocode(city).longitude)
#     return latitude, longitude
#
# def code_location(latitude: str, longitude: str, token_accu: str):
#     url_location_key = f'http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey={token_accu}&q={latitude},{longitude}&language=ru'
#     resp_loc = req.get(url_location_key, headers={"APIKey": token_accu})
#     json_data = json.loads(resp_loc.text)
#     code = json_data['Key']
#     return code
#
# def weather(cod_loc: str, token_accu: str):
#     url_weather = f'http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/{cod_loc}?apikey={token_accu}&language=ru&metric=True'
#     response = req.get(url_weather, headers={"APIKey": token_accu})
#     json_data = json.loads(response.text)
#     dict_weather = dict()
#     dict_weather['link'] = json_data[0]['MobileLink']
#     dict_weather['сейчас'] = {'temp': json_data[0]['Temperature']['Value'], 'sky': json_data[0]['IconPhrase']}
#     for i in range(len(json_data):1:):
#         time = 'через' + str(i) + 'ч'
#         dict_weather[time] = {'temp': json_data[i]['Temperature']['Value'], 'sky': json_data[i]['IconPhrase']}
# return dict_weather
#
#
# def print_weather(dict_weather, message):
#     bot.send_message(message.from_user.id, f'Разрешите доложить, Ваше сиятельство!'
#                                            f' Температура сейчас {dict_weather["сейчас"]["temp"]}!'
#                                            f' А на небе {dict_weather["сейчас"]["sky"]}.'
#                                            f' Температура через три часа {dict_weather["через3ч"]["temp"]}!'
#                                            f' А на небе {dict_weather["через3ч"]["sky"]}.'
#                                            f' Температура через шесть часов {dict_weather["через6ч"]["temp"]}!'
#                                            f' А на небе {dict_weather["через6ч"]["sky"]}.'
#                                            f' Температура через девять часов {dict_weather["через9ч"]["temp"]}!'
#                                            f' А на небе {dict_weather["через9ч"]["sky"]}.')
#     bot.send_message(message.from_user.id, f' А здесь ссылка на подробности '
#                                            f'{dict_weather["link"]}')

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