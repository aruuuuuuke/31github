import asyncio
import logging
from aiogram.types import Message, ContentType
from aiogram import Bot, Dispatcher
from core.handlers.basic import get_start, get_photo, get_hello
from core.settigns import settings
from aiogram.filters import ContentTypesFilter, Command
from aiogram import F
from core.filters.iscontact import IsTrueContact
from core.handlers.contact import get_true_contact, get_false_contact


token = '6560684648:AAE-Z17JMWefoiohcgujZu9KaL5WK0y3kpI'


async def start_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот запущен')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот остановлен')


async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'<b> привеет {message.from_user.first_name}. Рад тебя видеть!</b>')
    await message.answer(f'<s>привеет {message.from_user.first_name}. Рад тебя видеть!</s>')
    await message.reply(f'<tg-spoiler>привеет {message.from_user.first_name}. Рад тебя видеть!</tg-spoiler>')


async def start():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')

    dp = Dispatcher()

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_start, Command(commands=['start', 'run']))
    dp.message.register(get_photo, F.photo)
    dp.message.register(get_hello, F.text == 'Привет')
    dp.message.register(get_true_contact, ContentTypesFilter(content_types=[ContentType.CONTACT]), IsTrueContact())
    dp.message.register(get_false_contact, ContentTypesFilter(content_types=[ContentType.CONTACT]))
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
