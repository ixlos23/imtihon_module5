import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile
from db.config import engine

from bot.handlers.start import *

from bot.dispatcher import TOKEN, dp
from db.config import engine
from db.models import Base
from utils.middlewares import CustomMiddleware


def on_startup():
    Base.metadata.create_all(engine)


async def register_all_middleware():
    dp.update.middleware(CustomMiddleware())


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await register_all_middleware()
    dp.startup.register(on_startup)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())