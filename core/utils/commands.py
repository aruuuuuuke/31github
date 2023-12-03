from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Начало работы'
        ),
        BotCommand(
            command='help',
            description='Получить помощь'
        ),
        BotCommand(
            command='cancel',
            description='Отменить'
        ),
        BotCommand(
            command='inline',
            description='Инлайн кнопки'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())