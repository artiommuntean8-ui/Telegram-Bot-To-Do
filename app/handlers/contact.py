from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from app.services.validators import valid_contact
from app.db import insert_lead
from app.config import settings

router = Router()

class ContactForm(StatesGroup):
    name = State()
    contact = State()
    message = State()

@router.callback_query(F.data == "menu_contact")
async def start_contact(cb: CallbackQuery, state: FSMContext):
    await state.set_state(ContactForm.name)
    await cb.message.edit_text("Ваше имя:")
    await cb.answer()

@router.message(ContactForm.name)
async def get_name(msg: Message, state: FSMContext):
    name = msg.text.strip()
    if len(name) < 2:
        return await msg.answer("Слишком коротко. Введите имя ещё раз:")
    await state.update_data(name=name)
    await state.set_state(ContactForm.contact)
    await msg.answer("Ваш контакт (email или @username):")

@router.message(ContactForm.contact)
async def get_contact(msg: Message, state: FSMContext):
    contact = msg.text.strip()
    if not valid_contact(contact):
        return await msg.answer("Неверный формат. Пример: email@example.com или @username")
    await state.update_data(contact=contact)
    await state.set_state(ContactForm.message)
    await msg.answer("Сообщение (чем могу помочь):")

@router.message(ContactForm.message)
async def get_message(msg: Message, state: FSMContext):
    data = await state.get_data()
    message = msg.text.strip()
    if len(message) < 10:
        return await msg.answer("Добавьте деталей (минимум 10 символов).")
    await insert_lead(data["name"], data["contact"], message)
    await state.clear()
    await msg.answer("Спасибо! Я получил ваше сообщение и свяжусь с вами.")

    # Уведомление админа
    if settings.admin_id:
        await msg.bot.send_message(
            settings.admin_id,
            f"Новая заявка:\nИмя: {data['name']}\nКонтакт: {data['contact']}\nСообщение: {message}"
        )
