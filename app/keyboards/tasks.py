from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def tasks_keyboard(tasks):
    buttons = []
    for task_id, text, done in tasks:
        status = "✅" if done else "⬜️"
        buttons.append([InlineKeyboardButton(text=f"{status} {text}", callback_data=f"done_{task_id}")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)
