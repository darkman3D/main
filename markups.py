from telebot import types
source_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
source_markup_btn1 = types.KeyboardButton('Лестница')
source_markup_btn2 = types.KeyboardButton('Коридор')
source_markup.add(source_markup_btn1, source_markup_btn2)


AA_markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
AA_markup_btn1 = types.KeyboardButton('1')
AA_markup_btn2 = types.KeyboardButton('2')
AA_markup_btn3 = types.KeyboardButton('3')
AA_markup_btn4 = types.KeyboardButton('4')
AA_markup_btn5 = types.KeyboardButton('5')
AA_markup.add(AA_markup_btn1, AA_markup_btn2, AA_markup_btn3, AA_markup_btn4, AA_markup_btn5)

