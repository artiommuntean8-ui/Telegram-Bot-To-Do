from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Проекты", callback_data="menu_projects")],
        [InlineKeyboardButton(text="Навыки", callback_data="menu_skills")],
        [InlineKeyboardButton(text="Опыт", callback_data="menu_experience")],
        [InlineKeyboardButton(text="Контакты", callback_data="menu_contact")],
    ])
