from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType

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
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выбери кнопку")

loc_tel_poll_keyboard = ReplyKeyboardMarkup(keyboard =[
    [
        KeyboardButton(
            text='Отправить геолакацию',
            request_location=True
        )
    ],
    [
        KeyboardButton(
            text='Отправить контакт',
            request_poll=True
        )
    ],
    [
        KeyboardButton(
            text='Создать викторину',
            request_poll=KeyboardButtonPollType()
        )
    ],
], resize_keyboard=True, one_time_keyboard=False,
input_field_placeholder='Отправить геолокацию')
