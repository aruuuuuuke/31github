import json
from aiogram import Bot
from aiogram.types import Message

from core.keyboards.inline import select_mackbook
from core.keyboards.reply import reply_keyboard, loc_keyboard


async def get_inline(message:Message, bot:Bot):
    await message.answer(f'Hello, {message.from_user.first_name}. Here is inline buttons',
                         reply_markup=select_mackbook)


async def get_start(message: Message, bot: Bot):
    await message.answer(f'<s>привет {message.from_user.first_name}. Рад тебя видеть!</s>',
                         reply_markup=loc_keyboard)


async def get_location(message: Message, bot: Bot):
    await message.answer(f'Ты отправил геолокацию! \r\n'
                         f'Latitude: {message.location.latitude}\r\nLongitude: {message.location.longitude}')


async def get_photo(message: Message, bot: Bot):
    await message.answer(f'Oтлично, я сохраню ее себе. ')
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, 'photo.jpg')


async def get_hello(message: Message, bot: Bot):
    await message.answer(f'И тебе привет')
    json_str = json.dumps(message.dict(), default=str)
    print(json_str)
