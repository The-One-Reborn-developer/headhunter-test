from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from convert import convert
from keyboards import currency_keyboard, back_to_main_keyboard

router = Router()


class CurrencyConverter(StatesGroup):
    name=State()
    first_currency = State()
    second_currency = State()
    amount = State()


@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await state.set_state(CurrencyConverter.name)
    await message.answer(f"Добрый день, как Вас зовут 😺?")


@router.message(CurrencyConverter.name)
async def echo(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(CurrencyConverter.first_currency)

    content = f'Рад знакомству, {message.text}!\nВыберите валюту для конвертации ⏬ 🐈'

    await message.answer(content, reply_markup=currency_keyboard())


@router.callback_query(CurrencyConverter.first_currency)
async def dollar_callback(callback: CallbackQuery, state: FSMContext):
    await state.update_data(first_currency=callback.data)
    await state.set_state(CurrencyConverter.second_currency)
    
    content = f'Выберите валюту, к которой хотите конвертировать ⏬ 🐈'

    await callback.message.answer(content, reply_markup=currency_keyboard())


@router.callback_query(CurrencyConverter.second_currency)
async def dollar_callback(callback: CallbackQuery, state: FSMContext):
    await state.update_data(second_currency=callback.data)
    await state.set_state(CurrencyConverter.amount)

    await callback.message.answer('Введите сумму для конвертации ⏬ 🐈')


@router.message(CurrencyConverter.amount)
async def dollar_callback(message: Message, state: FSMContext):
    amount = message.text
    data = await state.get_data()
    first_currency = data['first_currency']
    second_currency = data['second_currency']

    conversion = await convert(first_currency, second_currency, float(amount))

    content = f'{amount} {first_currency} = {round(conversion, 2)} {second_currency} 😼'

    await state.clear()

    await message.answer(content, reply_markup=back_to_main_keyboard())


@router.callback_query(F.data == 'back')
async def back_to_main(callback: CallbackQuery, state: FSMContext):

    data = await state.get_data()
    
    name = data.get('name')
    
    content = f'Выберите валюту для конвертации ⏬ 🐈'

    await callback.message.edit_text(content, reply_markup=currency_keyboard())

    await state.set_state(CurrencyConverter.first_currency)
