import asyncio
from aiogram import Router, types, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.for_navigate import tasks_keyboard
from aiogram.utils.formatting import Bold, Underline, as_marked_section, as_section


tasks_router = Router()


TASK = []


@tasks_router.message(F.text == 'tasks')
@tasks_router.message(Command('tasks'))
async def tasks(message: types.Message):
    await message.reply('Please choose your action',
                        reply_markup=tasks_keyboard)


@tasks_router.message(F.text == 'check all')
async def check_all(message: types.Message):
    await message.reply('All your tasks',
                        reply_markup=types.ReplyKeyboardRemove())
    for i in range(len(TASK)):
        await asyncio.sleep(0.4)
        text = as_marked_section(
            'Task',
            as_section(Underline(i+1), Bold(TASK[i])),
            marker='✅ '
        )
        await message.answer(text.as_html())


class AddTask(StatesGroup):
    content = State()


@tasks_router.message(StateFilter(None), F.text == 'add a new task')
async def add_new_task(message: types.Message, state: FSMContext):
    await message.answer('Please enter your task',
                         reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(AddTask.content)


@tasks_router.message(AddTask.content, F.text)
async def add_task_to_list(message: types.Message, state: FSMContext):
    await state.update_data(content=message.text)
    await message.answer('Task has been added', reply_markup=tasks_keyboard)
    data = await state.get_data()
    await message.answer(str(data))
    TASK.append(data['content'])
    await state.clear()
