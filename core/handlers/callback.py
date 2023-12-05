from aiogram.types import CallbackQuery
from aiogram import Bot


async def select_mackbook(call: CallbackQuery, bot : Bot):
    model = call.data.split('_')[1]
    size = call.data.split('_')[2]
    chip = call.data.split('_')[3]
    chip = call.data.split('_')[3]
    year = call.data.split('_')[4]
    answer = f'{call.message.from_user.first_name}, you chosen the model {model} '\
             f'{size}, on chip{chip},{year}year'
    await call.message.answer(answer)
