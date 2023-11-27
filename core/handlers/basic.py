import json
from aiogram import Bot
from aiogram.types import Message
from core.keyboards.reply import reply_keyboard


async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'<b> привеет {message.from_user.first_name}. Рад тебя видеть!</b>',
                           reply_markup=reply_keyboard)


async def get_photo(message: Message, bot: Bot):
    await message.answer(f'Oтлично, я сохраню ее себе. ')
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, 'photo.jpg')


async def get_hello(message: Message, bot: Bot):
    await message.answer(f'И тебе привет')
    json_str = json.dumps(message.dict(), default=str)
    print(json_str)
