import asyncio

from aiogram import Bot, Dispatcher, F
from config_data.config import Config, load_config
from handlers import user_handlers
from handlers.user_handlers import set_main_menu

async def main() -> None:    

    config: Config = load_config()

    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()
    
    dp.include_router(user_handlers.router)

    dp.startup.register(set_main_menu)
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    

asyncio.run(main())    




