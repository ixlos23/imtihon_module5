import bs4
import requests
from aiogram import html, Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from aiogram.types import Message
from sqlalchemy import select, insert
from sqlalchemy.orm import Session

from Beautyfullsoup.beautyfullSoup import beautyfullsoup
from bot.buttons.reply_btn import *
from bot.state.state import StepState
from db.models import User

main_router = Router()

# @main_router.message(F.text == "Back", StepState.step3)


@main_router.message(CommandStart())
async def command_start_handler(message: Message, session: Session, state: FSMContext) -> None:
    # await state.clear()
    is_exists = session.execute(select(User).where(User.user_id == message.from_user.id)).scalar()
    if not is_exists:
        user = {
            "user_id": message.from_user.id,
            "username": message.from_user.username,
            "full_name": message.from_user.full_name
        }
        session.execute(insert(User).values(**user))
        session.commit()
    await message.answer_photo("https://telegra.ph/file/d7e54d1749e42bc943502.png", caption="""Assalomu alaykum ! 
Bu bo'timiz sizga kunlik qiladigan 🏋️ mashqlarni ko'rsatib beradi""" , reply_markup=start_btn())
    await state.set_state(StepState.step1)


@main_router.message(StepState.step1, F.text)
async def start_handler(message: Message, session: Session, state: FSMContext) -> None:

    if message.text == filial:
        await message.answer_location(latitude=41.304476, longitude=69.253043, reply_markup=start_btn())
    if message.text == start:
        await message.answer("Quydagilardan birontasini tanlang 👇🏿", reply_markup=men_women())
        await state.set_state(StepState.step2)
    if message.text == admin:
        await message.answer("https://t.me/Absaitov_Dilshod")
    if message.text == newpost:
        result = beautyfullsoup()
        await message.answer(result)

# await state.set_state(BackState.back1)

# @main_router.message(F.text == "🔙 back")
# async def ortga_hndlr(message: Message, state: FSMContext) -> None:
#     await state.clear()
#     await message.answer("Back", reply_markup=start_btn())


@main_router.message(StepState.step2, F.text)
async def men_women_handler(message: Message, session: Session, state: FSMContext) -> None:
    if message.text == men:
        await message.answer_photo("https://telegra.ph/file/362c72ebe03d252c905bf.png", caption="Quydagilarni birontasini tanlang 👇🏿", reply_markup=month_men())
        await state.set_state(StepState.step3)
    if message.text == women:
        await message.answer_photo("https://telegra.ph/file/bcb44486feddc2f0507af.png", caption="Quydagilarni birontasini tanlang 👇🏿" , reply_markup=month_women())
        await state.set_state(StepState.step4)


@main_router.message(StepState.step3, F.text)
async def month_men_handler(message: Message, session: Session, state: FSMContext) -> None:
    if message.text == oy1:
        await message.answer("Hafta kunlaridan birontasini tanlang", reply_markup=hafta_kn())


@main_router.message(StepState.step4, F.text)
async def month_women_handler(message: Message, session: Session, state: FSMContext) -> None:
    await message.answer("vaqt yetmadi ")
