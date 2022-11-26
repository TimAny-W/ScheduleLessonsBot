from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

user_kb = ReplyKeyboardMarkup(resize_keyboard=True).row(
    KeyboardButton('Пн'),
    KeyboardButton('Вт'),
    KeyboardButton('Ср'),
    KeyboardButton('Чт'),
    KeyboardButton('Пт'),
    KeyboardButton('Сб'),


).row(
    KeyboardButton('Сегодня'),
    KeyboardButton('Завтра'),
)
