import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from decouple import config
from handlers.private import private_router
from handlers.tasks import tasks_router
from optional.options import private


async def main():
    bot = Bot(token=config('TOKEN'),
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    dp.include_routers(private_router, tasks_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private,
                              scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot)


asyncio.run(main())
