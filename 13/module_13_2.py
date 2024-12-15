from aiogram import Bot, Dispatcher, types
from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import asyncio
from aiogram.fsm.storage.memory import MemoryStorage

start_router = Router()


@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью')


@start_router.message(F.text)
async def cmd_start_3(message: Message):
    await message.answer('Введите команду /start, чтобы начать общение')


async def main():
    api = ''
    bot = Bot(token=api)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(start_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
