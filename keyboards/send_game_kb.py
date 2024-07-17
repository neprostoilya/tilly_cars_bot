from aiogram.types import WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config.configuration import URL


def send_game_kb():
    """
    Send game kb
    """
    builder = InlineKeyboardBuilder()
    
    builder.button(
        text='🕹️ Play',
        web_app=WebAppInfo(
            url='https://html5.gamedistribution.com/5d513da2cf424e5e907b734848a3ec5d/'
        )
    )
    
    return builder.as_markup()