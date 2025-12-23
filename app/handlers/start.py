from aiogram import Router, F
from aiogram.types import Message
from app.db import init_db

router = Router()

@router.message(F.text == "/start")
async def cmd_start(message: Message):
    await init_db()
    await message.answer("Привет! Я твой To‑Do бот. Напиши задачу, и я её сохраню.")
