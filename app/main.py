import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from app.config import settings
from app.handlers import start, projects, skills, experience, contact, admin
from app.db import init_db

async def on_startup(bot: Bot):
    commands = [
        BotCommand(command="start", description="Запуск бота"),
        BotCommand(command="menu", description="Главное меню"),
    ]
    await bot.set_my_commands(commands)

async def main():
    bot = Bot(settings.bot_token)
    dp = Dispatcher()

    # Регистрация роутеров
    dp.include_routers(
        start.router,
        projects.router,
        skills.router,
        experience.router,
        contact.router,
        admin.router,
    )

    await init_db( )
    await on_startup(bot)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
