import requests
import re
import telebot
import config
import markups as m
bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    chat_id = message.chat.id
    text = message.text
    msg = bot.send_message(chat_id, '''Ты стоишь в холле колледжа. Зачем ты сюда пришел и что собрался делать, меня не интересует, раз пришел - значит нужно.
Справа от тебя закрытый гардероб, слева стена объявлений со слотом под лис товку с Милосом. Ты поднимаешься по трем ступенькам и видишь на 3 часа вахту и маникюрную. 
Слева лестница для передвижения между этажами и длинный коридор спереди.
Куда отправишься, друг?''', reply_markup=m.source_markup)
    bot.register_next_step_handler(msg, start_hall)


@bot.message_handler(content_types=['text', 'photo'])
def start_hall(message):
    chat_id = message.chat.id
    text = message.text
    if message.text == 'Лестница':
        m1 = bot.send_message(chat_id, 'На какой этаж ты поднимешься 2, 3, 4, 5?', reply_markup=m.AA_markup)
        bot.register_next_step_handler(m1, less)
    elif message.text == 'Коридор':
        m2 = bot.send_message(chat_id, 'На этом этаже нет ничего, что могло бы привлечь твоё внимание, кроме туалета и бездны в конце коридора, ведущей в неизвестность')
        bot.register_next_step_handler(m2, start_hall)
    return


def les_corr(message):
    chat_id = message.chat.id
    text = message.text
    msq = bot.send_message(chat_id, 'На этом этаже нет ничего, что могло бы привлечь твоё внимание, кроме туалета и бездны в конце коридора, ведущей в неизвестность.')
    bot.register_next_step_handler(msq, les_corr)
    return


def less(message):
    chat_id = message.chat.id
    text = message.text
    if message.text == '2':
        m1 = bot.send_message(chat_id, '''После того как ты поднялся ты увидел библиотеку по правую руку, убежище фиксиков прямо перед собой(Даже не пытайся их призвать, эти мобы сами появятся когда нужно) и 
длинный коридор со спортивным залом в конце''')
    elif message.text == '3':
        m2 = bot.send_message(chat_id, 'Сразу после лестницы справа от тебя актовый зал и очередной длинный коридор с аудиториями, тут ничего интересного')
    elif message.text == '4':
        m3 = bot.send_message(chat_id, '''На этом этаже только аудитории и ничего интересного кроме кабинета психолога сразу за поворотом в конце коридора и прекрасного вида на задний двор колледжа из окон.
Куда хочешь отправиться дальше''')
    elif message.text == '5':
        m4 = bot.send_message(chat_id, '''Об этом месте ходило множество легенд, но оно так и не было задокументировано учеными, а очевидцы уже либо умерли, 
либо долживают остатки своих дней с проблемами восприятия реальности.
А так же там ебутся пожелые коты''')
    return


bot.polling()
