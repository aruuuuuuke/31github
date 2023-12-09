from aiogram.types import CallbackQuery
from aiogram import Bot


async def select_mackbook(call: CallbackQuery, bot: Bot):
    try:
        model = call.data.split('_')[1]
        size = call.data.split('_')[2]
        chip = call.data.split('_')[3]
        year = call.data.split('_')[4]

        answer = f'{call.message.from_user.first_name}, you chose the model {model}, ' \
                 f'{size}, on chip {chip}, {year} year'

        await bot.send_message(chat_id=call.message.chat.id, text=answer)

    except IndexError:
        # Обработка случая, когда данные коллбека не соответствуют ожидаемому формату
        error_message = "Sorry, something went wrong. Please try again."
        await bot.send_message(chat_id=call.message.chat.id, text=error_message)
