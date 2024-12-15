from aiogram import Bot, Dispatcher, types
from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.methods import GetMyName
from aiogram.types import Message
from aiogram.filters.state import StatesGroup, State
import asyncio
from aiogram.fsm.storage.memory import MemoryStorage

api = ''
bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())
start_router = Router()

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@start_router.message(F.text == 'Calories')
async def set_age(message: Message,state: FSMContext):
    await message.answer('Введите свой возраст')
    await state.set_state(UserState.age)

@start_router.message(UserState.age)
async def set_growth(message: Message,state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост')
    await state.set_state(UserState.growth)

@start_router.message(UserState.growth)
async def set_weight(message: Message,state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await state.set_state(UserState.weight)

@start_router.message(UserState.weight)
async def send_calories(message: Message,state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    # для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;
    calories = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age'])
    await message.answer(f'Ваша норма калорий: {calories}')
    await state.clear()


@start_router.message(F.text)
async def cmd_start_3(message: Message):
    await message.answer('Введите текст "Сalories" , для расчета нормы калорий')


async def main():
    dp.include_router(start_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
