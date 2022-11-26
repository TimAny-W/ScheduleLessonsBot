from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

from aiogram.dispatcher.filters import Text

from config import schedule
from buttons import user_kb

import logging
import datetime
import os

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_message(message: types.Message):
    await message.answer("Привет!\n Я бот который отправляет тебе твое расписание!", reply_markup=user_kb)


@dp.message_handler(Text(equals='сегодня', ignore_case=True))
async def today(message: types.Message):
    msg = schedule[
        list(schedule.keys())[datetime.datetime.now().weekday()]
    ]
    await message.answer(f'<b>{msg}</b>', parse_mode=types.ParseMode.HTML)


@dp.message_handler(Text(equals='завтра', ignore_case=True))
async def tomorrow(message: types.Message):
    date = datetime.datetime.now().weekday() + 1
    msg = ''

    if date > 6:
        msg = schedule[
            list(schedule.keys())[0]
        ]

    else:
        msg = schedule[
            list(schedule.keys())[date]
        ]

    await message.answer(f'<b>{msg}</b>', parse_mode=types.ParseMode.HTML)


@dp.message_handler(Text(equals=schedule.keys(), ignore_case=True))
async def send_schedule(message: types.Message):
    msg = schedule[message.text]

    await message.answer(f'<b>{msg}</b>', parse_mode=types.ParseMode.HTML)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
