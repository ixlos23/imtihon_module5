import logging
import executor
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.context import FSMContext
import aiosmtplib
from email.mime.text import MIMEText
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage
from py_fastapi_logging.middlewares.logging import LoggingMiddleware

load_dotenv()

API_TOKEN = '7314679449:AAH8XcL0CpiSDYNJ7xJLe4Gt-Z-i8XIDCos' # noqa
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = int(465)
EMAIL_USER = 'izzatmatkarimov090@gmail.com'
EMAIL_PASSWORD = 'lenovocorei5' # noqa

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware()) # noqa


class Form(StatesGroup):
    email = State()
    message = State()


@dp.message(commands='start')
async def cmd_start(message: types.Message):
    await Form.email.set() # noqa
    await message.reply("Assalomu alaykum! Menga elektron pochta manzilingizni kiriting:") # noqa


@dp.message(state=Form.email)
async def process_email(message: types.Message, state: FSMContext):
    await state.update_data(email=message.text)
    await Form.next() # noqa
    await message.reply("Rahmat! Endi, yuboriladigan xabarni kiriting:") # noqa


@dp.message(state=Form.message)
async def process_message(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    email = user_data['email']
    message_text = message.text

    await send_email(email, message_text)

    await message.reply("Xabar muvaffaqiyatli yuborildi!") # noqa
    await state.finish() # noqa


async def send_email(email, message_text):
    msg = MIMEText(message_text)
    msg['Subject'] = 'Telegram Bot Xabari' # noqa
    msg['From'] = EMAIL_USER
    msg['To'] = email

    async with aiosmtplib.SMTP(hostname=SMTP_SERVER, port=SMTP_PORT, use_tls=True) as server:
        await server.login(EMAIL_USER, EMAIL_PASSWORD)
        await server.send_message(msg)


@dp.message(commands='cancel', state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    await state.finish() # noqa
    await message.reply('Amal bekor qilindi.', reply=False) # noqa

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True) # noqa
