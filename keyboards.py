from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def currency_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="RUB ₽",
                    callback_data="RUB"
                ),
                InlineKeyboardButton(
                    text="USD $",
                    callback_data="USD"
                ),
                InlineKeyboardButton(
                    text="EUR €",
                    callback_data="EUR"
                ),
                InlineKeyboardButton(
                    text="CNY ¥",
                    callback_data="CNY"
                )
            ]
        ]
    )


def back_to_main_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="⬅️ Назад в главное меню",
                    callback_data="back"
                )
            ]
        ]
    )