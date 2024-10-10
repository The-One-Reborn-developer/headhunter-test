from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def main_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Добавить RSS источник ➕",
                    callback_data="add_rss"
                )
            ],
            [
                InlineKeyboardButton(
                    text="Получить новости за последний час ℹ️",
                    callback_data="last_hour"
                )
            ],
            [
                InlineKeyboardButton(
                    text="Получить новости за последние сутки ℹ️",
                    callback_data="last_day"
                )
            ],
            [
                InlineKeyboardButton(
                    text="Помощь ❓",
                    callback_data="help"
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