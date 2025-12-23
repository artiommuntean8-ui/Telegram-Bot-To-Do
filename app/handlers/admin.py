from aiogram import Router, F
from aiogram.types import Message
from app.config import settings
import aiosqlite
from app.db import DB_PATH

router = Router()

def is_admin(user_id: int) -> bool:
    return settings.admin_id and user_id == settings.admin_id

@router.message(F.text == "/leads")
async def show_leads(msg: Message):
    if not is_admin(msg.from_user.id):
        return await msg.answer("Доступ запрещён.")
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT name, contact, message, created_at FROM leads ORDER BY id DESC LIMIT 10") as cur:
            rows = await cur.fetchall()
    if not rows:
        return await msg.answer("Заявок пока нет.")
    text = "\n\n".join([f"{r[3]} — {r[0]} ({r[1]}):\n{r[2]}" for r in rows])
    await msg.answer(text)
