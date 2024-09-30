from aiogram import types


keyboard = types.ReplyKeyboardMarkup(
    keyboard=[
        [
            types.KeyboardButton(text='options'),
            types.KeyboardButton(text='tasks'),
        ],
        [
            types.KeyboardButton(text='about'),
            types.KeyboardButton(text='links')
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='All commands'
)


tasks_keyboard = types.ReplyKeyboardMarkup(
    keyboard=[
        [
            types.KeyboardButton(text='check all')
        ],
        [
            types.KeyboardButton(text='add a new task')
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Actions...'
)
