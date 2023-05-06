from aiogram import Bot, Dispatcher
from aiogram.types import Message
import asyncio

import BOT_TOKEN

async def say_start(message: Message, bot: Bot):
    await message.answer('Скажи - я скажу')

async def echo_msg(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, message.text)

async def start():
   bot = Bot(token=BOT_TOKEN)
   dp = Dispatcher()

   dp.message.register(say_start)
   dp.message.register(echo_msg)

   try:
      await dp.start_polling(bot)
   finally:
      await bot.session_close()

if __name__ == '__main__':
    asyncio.run(start())
