import asyncio
import logging
import sys

from aiogram import Dispatcher
from aiogram import Bot

from config.configuration import URL
from handlers import commands, send_game, options
from config.instance import bot


# async def on_startup(bot: Bot):
#     """
#     Main button in bot for game
#     """
#     await bot.set_chat_menu_button(
#         menu_button=MenuButtonWebApp(text="🕹️ Play", web_app=WebAppInfo(url=URL))
#     )


async def main():
    """ 
    Main 
    """
    dp = Dispatcher()
    
    dp.include_routers(commands.router_commands)
    dp.include_routers(send_game.router_send_game)
    # dp.include_routers(options.router_options)

    await bot.delete_webhook(drop_pending_updates=True)
    await asyncio.gather(dp.start_polling(bot))

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())