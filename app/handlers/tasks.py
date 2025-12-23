from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from app.db import add_task, get_tasks, complete_task
from app.keyboards.tasks import tasks_keyboard

router = Router()

@router.message(F.text)
async def add_new_task(message: Message):
    await add_task(message.from_user.id, message.text)
    tasks = await get_tasks(message.from_user.id)
    await message.answer("Задача добавлена!", reply_markup=tasks_keyboard(tasks))

@router.callback_query(F.data.startswith("done_"))
async def mark_done(cb: CallbackQuery):
    task_id = int(cb.data.split("_")[1])
    await complete_task(task_id)
    tasks = await get_tasks(cb.from_user.id)
    await cb.message.edit_text("Ваши задачи:", reply_markup=tasks_keyboard(tasks))
    await cb.answer("Отмечено как выполнено ✅")
