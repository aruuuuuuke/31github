from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='ряд 1, кнопка 1'
        ),
        KeyboardButton(
            text='ряд 1, кнопка 2'
        ),
        KeyboardButton(
            text='ряд 1, кнопка 3'
        )
    ],
    [
        KeyboardButton(
            text='ряд 2, кнопка 1'
        ),
        KeyboardButton(
            text='ряд 2, кнопка 2'
        ),
        KeyboardButton(
            text='ряд 2, кнопка 3'
        ),
        KeyboardButton(
            text='ряд 2, кнопка 4'
        ),
    ],
    [
        KeyboardButton(
            text='ряд 3, кнопка 1'
        ),
        KeyboardButton(
            text='ряд 3, кнопка 2'
        ),
        KeyboardButton(
            text='ряд 3, кнопка 3'
        ),
        KeyboardButton(
            text='ряд 3, кнопка 4'
        ),
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выбери кнопку", selective = True)
