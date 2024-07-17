from aiogram import Router, F
from aiogram.types import Message
from aiogram.utils.markdown import hbold


from keyboards.send_game_kb import send_game_kb


router_send_game = Router()

@router_send_game.message(F.text == "🕹️ Play")
async def send_game_handler(message: Message):
    """
    Send game handler
    """
    await message.answer(
        text=hbold('Let`s play a game'),
        reply_markup=send_game_kb()
    )