from aiogram import Bot, Dispatcher, types
from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.methods import GetMyName
from aiogram.types import Message, InlineKeyboardButton
from aiogram.types import (Message, ReplyKeyboardMarkup, KeyboardButton,
                           ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup)
from aiogram.filters.state import StatesGroup, State
import asyncio
from aiogram.fsm.storage.memory import MemoryStorage
from numpy.f2py.cfuncs import callbacks

api = ''
bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())
start_router = Router()

button_1 = KeyboardButton(text='Рассчитать')
button_2 = KeyboardButton(text='Информация')
kb_list = [[button_1], [button_2]]
kb = ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True)

inline_kb_list = [
    [InlineKeyboardButton(text='Расчитать норму калорий', callback_data='calories')],
    [InlineKeyboardButton(text='Формулы расчета', callback_data='formulas')]
]
in_kb = InlineKeyboardMarkup(inline_keyboard=inline_kb_list)


@start_router.message(F.text == 'Рассчитать')
async def main_menu(message: Message):
    await message.answer('Выберите опцию:', reply_markup=in_kb)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@start_router.callback_query(F.data.startswith('formulas'))
async def set_age(call):
    await call.answer()
    await call.message.answer('для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;')


@start_router.callback_query(F.data.startswith('calories'))
async def set_age(call, state: FSMContext):
    await call.answer()
    await call.message.answer('Введите свой возраст')
    await state.set_state(UserState.age)


@start_router.message(UserState.age)
async def set_growth(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост')
    await state.set_state(UserState.growth)


@start_router.message(UserState.growth)
async def set_weight(message: Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await state.set_state(UserState.weight)


@start_router.message(UserState.weight)
async def send_calories(message: Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calories = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age'])
    await message.answer(f'Ваша норма калорий: {calories}')
    await state.clear()


@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью', reply_markup=kb)


async def main():
    dp.include_router(start_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())