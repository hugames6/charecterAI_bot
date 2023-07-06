from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

help = KeyboardButton('Помощь 🆘')
choise = KeyboardButton('Давай! ▶️')
take_choise = KeyboardButton('Выбрать персонажа 🍫', web_app=WebAppInfo(url='https://hugames6.github.io/characterAITEST.github.io/'))
next1 = KeyboardButton('Дальше ▶️')
bug = KeyboardButton('Сообщить об ошибке 📣')
on_start = KeyboardButton('В начало ⭐️')
buffer = KeyboardButton('Можно задать вопрос? ❔')

client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
choose = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
next_msg = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
help_wanted = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
buffer_zone = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)


client.row(next1, help)
choose.add(take_choise)
next_msg.row(choise, help)
help_wanted.row(on_start, bug)
buffer_zone.row(buffer, take_choise)
