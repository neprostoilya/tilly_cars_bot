from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.markdown import hbold


def options_menu_kb(sound_enabled: bool):
    """
    Options menu keyboard
    """
    builder = InlineKeyboardBuilder()
    
    if sound_enabled:
        builder.button(
            text='🔇 Sound Off',
            callback_data='toggle_sound'
        )
    else:
        builder.button(
            text='🔊 Sound On' ,
            callback_data='toggle_sound'
        )
            
    return builder.as_markup()