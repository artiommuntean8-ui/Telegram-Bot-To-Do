from aiogram import Router, F
from aiogram.types import CallbackQuery

router = Router()

SKILLS = [
    "Python (async, OOP, testing)",
    "aiogram 3.x",
    "SQL (SQLite/PostgreSQL)",
    "Git/GitHub, Docker",
    "REST APIs, webhooks",
]

@router.callback_query(F.data == "menu_skills")
async def show_skills(cb: CallbackQuery):
    await cb.message.edit_text("Навыки:\n- " + "\n- ".join(SKILLS))
    await cb.answer()
