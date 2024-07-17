from aiogram import Bot
from aiogram.enums import ParseMode
from config.configuration import TOKEN_BOT

from aiogram.client.bot import DefaultBotProperties


bot = Bot(
    token=TOKEN_BOT,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)