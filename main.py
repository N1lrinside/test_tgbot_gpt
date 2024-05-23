import asyncio
import logging
import sys
import os
from aiogram import Dispatcher, Bot
from aiogram.enums import ParseMode
from dotenv import load_dotenv
from app.handlers import rt
async def main() -> None:
    load_dotenv()
    bot = Bot(token=os.getenv('TG_TOKEN'), parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_router(rt)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')

