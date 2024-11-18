from aiogram import Bot, Dispatcher, F
from dotenv import load_dotenv
import os
import logging
import asyncio
from handlers import router as handler_router

async def main():
    logging.basicConfig(level=logging.INFO)
    load_dotenv()
    TOKEN = os.getenv('TOKEN')
    bot = Bot(TOKEN)
    dp = Dispatcher()
    dp.include_router(handler_router)
    await dp.start_polling(bot)



if __name__ == '__main__':
    asyncio.run(main())
