import asyncio
from aiogram import Bot, Dispatcher
from app.config import settings
from app.handlers import start, tasks
from app.db import init_db

async def main():
    bot = Bot(settings.bot_token)
    dp = Dispatcher()

    dp.include_routers(start.router, tasks.router)

    await init_db()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
