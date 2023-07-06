from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from bot import bot
from keyboards import client, choose, next_msg, help_wanted, buffer_zone
from database.db import sql_add_data, sql_get_data_from_bots, sql_add_question
from ai_module import ai

from analytic.analytic import user_choise, user_registration, user_send_question, send_answer_to_user, we_get_API_answer 

import time

char = ""

async def get_date():
    loc_time = time.localtime(time.time())
    date = time.strftime('%d.%m.%Y %H:%M:%S', loc_time)
    return date

async def get_id():
    id = int(time.time()) + 10800
    return id

class FSMAnswering(StatesGroup):
    quest = State()
    bot_answ = State()

async def help(message : types.Message):
    await bot.send_message(message.from_user.id, 'Чем могу помочь?', reply_markup=help_wanted)

async def start(message : types.Message):
    await bot.send_message(message.from_user.id, 'Привет! Я - бот на пободии character.ai, и создан для взаимодействия с пользователем.', reply_markup=client)
    a = await sql_add_data(user_id=message.from_user.id, username=message.from_user.username, name=message.from_user.first_name, surname=message.from_user.last_name, date=await get_date())
    if a != True:
        await user_registration(user_id=message.from_user.id)

async def talk(message : types.Message):
    await bot.send_message(message.chat.id, 'Ты можешь написать любой свой тектовый запрос, и ИИ ответит тебе на него. Но сначала тебе нужно выбрать персонажа!', reply_markup=next_msg)

async def choise(message : types.Message):
    await bot.send_message(message.from_user.id, 'У тебя на выбор есть 2 персонажа - игровой персонаж Марио, и физик-теоритик Альберт Эйнштейн! Нажми на кнопку ниже и выбери!', reply_markup=choose)

async def web_data_choise(message : types.Message): 
    global char
    char = message.web_app_data.data
    await user_choise(user_id=message.from_user.id)
    hello = await sql_get_data_from_bots(char)
    if char == 'mario':
        photo = open('E:\\VS_CODE\\TGBots\\characterAI_TEST\\templates\\mario.png', 'rb')
        await bot.send_photo(message.chat.id, photo=photo, caption=hello, reply_markup=buffer_zone)
    elif char == 'einstein':
        photo = open('E:\\VS_CODE\\TGBots\\characterAI_TEST\\templates\\albert.png', 'rb')
        await bot.send_photo(message.chat.id, photo=photo, caption=hello, reply_markup=buffer_zone)

async def start_talking(message : Message):
    await bot.send_message(message.chat.id, 'Какой у тебя ко мне вопрос?')
    await FSMAnswering.quest.set()

async def user_question(message : Message, state : FSMContext):
    item = message.text
    await state.update_data({f"question": item})
    await user_send_question(user_id=message.from_user.id)
    await bot.send_message(message.chat.id, 'Обрабатываю твой вопрос!')
    if char == 'mario':
        answer = await ai.get_mario_answer(item)
        await we_get_API_answer(user_id=message.from_user.id)
        await sql_add_question(iter_id=await get_id(), user_id=message.from_user.id, bot_name='mario', user_question=item, bot_answer=answer, time=await get_date())
        await send_answer_to_user(user_id=message.from_user.id)
    elif char == 'einstein':
        answer = await ai.get_einstein_answer(item)
        await we_get_API_answer(user_id=message.from_user.id)
        await sql_add_question(iter_id=await get_id(), user_id=message.from_user.id, bot_name='einstein', user_question=item, bot_answer=answer, time=await get_date())
        await send_answer_to_user(user_id=message.from_user.id)
    await bot.send_message(message.chat.id, f'{answer}', reply_markup=buffer_zone)
    await state.finish()


def reg_hendlers_user(dispatch : Dispatcher):
    dispatch.register_message_handler(help, Text(contains='Помощь', ignore_case=True))
    dispatch.register_message_handler(start, commands=['start'])
    dispatch.register_message_handler(choise, Text(contains='Давай!', ignore_case=True))
    dispatch.register_message_handler(web_data_choise, content_types=['web_app_data'])
    dispatch.register_message_handler(talk, Text(contains='Дальше', ignore_case=True))
    dispatch.register_message_handler(user_question, state=FSMAnswering.quest)
    dispatch.register_message_handler(start_talking, Text(contains='Можно задать вопрос?', ignore_case=True), state=None)