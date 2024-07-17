# from aiogram import Router, F
# from aiogram.types import Message, CallbackQuery
# from aiogram.utils.markdown import hbold
# from aiogram.fsm.context import FSMContext

# from keyboards.options_kb import options_menu_kb
# from utils.playwright import toggle_media_state

# router_options = Router()

# @router_options.message(F.text == "⚙️ Options")
# async def menu_options_handler(message: Message, state: FSMContext):
#     """
#     Menu options handler
#     """
#     data: dict = await state.get_data()
    
#     state_sound: bool = data.get('state_sound', True)

#     await message.answer(
#         text=hbold('Choose options:'),
#         reply_markup=options_menu_kb(
#             sound_enabled=state_sound,
#         )
#     )
    
#     await state.update_data(
#         state_sound = state_sound,
#     )
    
# @router_options.callback_query(F.data == "toggle_sound")
# async def change_state_sound_handler(call: CallbackQuery, state: FSMContext):
#     """
#     Change state sound handler
#     """
#     data: dict = await state.get_data()
    
#     state_sound: bool = data.get('state_sound', True)

#     await toggle_media_state(not state_sound)

#     await call.message.edit_reply_markup(
#         reply_markup=options_menu_kb(
#             sound_enabled=notstate_sound
#         )
#     )

#     await state.update_data(
#         state_sound=not state_sound,
#     )