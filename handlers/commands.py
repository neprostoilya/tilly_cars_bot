from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.markdown import hbold


from keyboards.menu_kb import menu_kb


router_commands = Router()


@router_commands.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    """
    Reaction on command '/start'
    """
    username: str = message.from_user.full_name
    
    await message.answer(
        text=f'Hello {hbold(username)}.',
        reply_markup=menu_kb()
    )


@router_commands.message(Command('about'))
async def command_about_handler(message: Message) -> None:
    """
    Reaction on command '/about'
    """
    await message.answer(
        text=f'This is a bot for playing Tinny Cars'
    )


@router_commands.message(Command('help'))
async def command_help_handler(message: Message) -> None:
    """
    Reaction on command '/help'
    """
    await message.answer(
        text=f"Have any questions? write to @neprostoilya"
    )