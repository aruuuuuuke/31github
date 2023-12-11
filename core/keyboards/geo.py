from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram import Bot
from aiogram.types import ParseMode

# Инициализация бота и диспетчера
bot = Bot(token='YOUR_BOT_TOKEN')
dp = Dispatcher(bot)


# Обработка сообщения с геолокацией
@dp.message_handler(content_types=types.ContentType.LOCATION)
async def handle_location(message: types.Message):
    location = message.location
    latitude = location.latitude
    longitude = location.longitude

    # Ваш код обработки геолокации
    await message.reply(f'Принял геолокацию. Широта: {latitude}, Долгота: {longitude}')

# Запуск бота
if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
