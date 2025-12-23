from aiogram import Router, F
from aiogram.types import CallbackQuery
from app.services.repo import PROJECTS

router = Router()

@router.callback_query(F.data == "menu_projects")
async def show_projects(cb: CallbackQuery):
    text_lines = []
    for p in PROJECTS:
        links = []
        if p.repo: links.append(f"[Repo]({p.repo})")
        if p.demo: links.append(f"[Demo]({p.demo})")
        text_lines.append(
            f"• {p.title}\n"
            f"  Описание: {p.description}\n"
            f"  Стек: {', '.join(p.stack)}\n"
            f"  {' | '.join(links) if links else 'Ссылки: нет'}\n"
        )
    await cb.message.edit_text("\n\n".join(text_lines), parse_mode="Markdown")
    await cb.answer()
