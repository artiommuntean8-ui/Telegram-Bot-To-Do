from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from app.keyboards.menu import main_menu

router = Router()

@router.message(F.text.in_({"/start", "/menu"}))
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Я бот-портфолио Мунтеана. Выберите раздел:",
        reply_markup=main_menu()
    )

@router.callback_query(F.data.startswith("menu_"))
async def open_section(cb: CallbackQuery):
    mapping = {
        "menu_projects": "Раздел проектов. Ниже — мои работы.",
        "menu_skills": "Мои ключевые навыки и стек.",
        "menu_experience": "Опыт и достижения.",
        "menu_contact": "Оставьте сообщение — я свяжусь.",
    }
    await cb.message.edit_text(mapping.get(cb.data, "Раздел"), reply_markup=main_menu())
    await cb.answer()
