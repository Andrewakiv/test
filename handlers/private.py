from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command, or_f
from aiogram.utils.formatting import as_list, as_marked_section, Bold, TextLink
from keyboards.for_navigate import keyboard


private_router = Router()


@private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.reply('you started work with our bot', reply_markup=keyboard)


@private_router.message(or_f(Command('options'), F.text == 'options'))
async def options(message: types.Message):
    await message.reply('all our options')


@private_router.message(F.text == 'links')
async def links(message: types.Message):
    text = as_marked_section(
        Bold('All our links'),
        TextLink('Google meet tech', url='https://meet.google.com/mht-tydj-emg'),
        TextLink('Google meet soft', url='https://meet.google.com/paf-ypaw-xwi'),
        TextLink('LMS', url=r'https://edu.goiteens.com/uk/dl/%D0%9F%D1%96%D0%B4%D0%B3%D1%80%D1%83%D0%BF%D0%B0_1_GoITeens_UA_PYTHON_1y_13_20_04_24_20607988?rtr=true'),
        TextLink('Support bot', url='https://t.me/GoITeens_Study_bot'),
        marker='✅ '
    )
    await message.reply(text.as_html())


@private_router.message(Command('about'))
async def about(message: types.Message):
    await message.reply('Simple bot to manage your tasks')
