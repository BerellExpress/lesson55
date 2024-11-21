import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

api =
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


#@dp.message_handler(text={'Urban'})
#async def urban_massage(massage):
#    print("Urban massage")
#    await massage.answer('Urban massage')

@dp.message_handler(commands={'start'})
async def start_massage(massage):
    print('Хозяин, кто-то активировал секретную команду ;-ъ')
    await massage.answer('Привет! Я бот, помогающий твоему здоровью.')

@dp.message_handler()
async def all_massage(massage):
    print('Хозяин, какая-то челядь пытается общаться со Скайнетом, что делаем?')
    await massage.answer('Введите команду /start, чтобы начать общение')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
