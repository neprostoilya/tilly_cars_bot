from aiogram.utils.keyboard import ReplyKeyboardBuilder


def menu_kb():
    """
    Main menu keyboard
    """
    builder = ReplyKeyboardBuilder()
    
    builder.button(
        text='🕹️ Play'
    )   
    
    # builder.button(
    #     text='⚙️ Options'
    # )     
    
    return builder.as_markup(
        resize_keyboard=True
    )