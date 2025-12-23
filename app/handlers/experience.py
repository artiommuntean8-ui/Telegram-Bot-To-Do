from aiogram import Router, F
from aiogram.types import CallbackQuery

router = Router()

EXPERIENCE = [
    "Учебные проекты: боты, утилиты, интеграции",
    "Контент: мини-уроки, разборы кода",
    "Решение практических задач для семьи/друзей",
]

@router.callback_query(F.data == "menu_experience")
async def show_experience(cb: CallbackQuery):
    await cb.message.edit_text("Опыт:\n- " + "\n- ".join(EXPERIENCE))
    await cb.answer()
