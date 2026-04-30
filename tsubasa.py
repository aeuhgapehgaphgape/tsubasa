print("BOT STARTED")

import asyncio
from aiogram import Bot, Dispatcher

bot = Bot("ТВОЙ_ТОКЕН")
dp = Dispatcher()

async def main():
    print("RUNNING...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())