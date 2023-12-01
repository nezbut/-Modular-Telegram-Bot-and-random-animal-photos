from config_data.config import load_config
from aiogram import Bot, Dispatcher
from handlears import user_handlears, other_handlears
import logging
import asyncio

async def main():
    logging.basicConfig(level=logging.INFO)
    config = load_config()
    bot = Bot(token=config.telegram_bot.bot_token)
    dp = Dispatcher()

    dp.include_routers(
        user_handlears.router,
        other_handlears.router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
