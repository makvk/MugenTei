import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os
from handlers.common import router as common_router
from handlers.main_buttons import router as main_buttons_router
from handlers.figures_callback import router as figures_callback_router
from handlers.school_program_callback import router as school_program_callback_router

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def main():
    bot = Bot(token = BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(main_buttons_router)
    dp.include_router(figures_callback_router)
    dp.include_router(school_program_callback_router)
    dp.include_router(common_router)

    print("Есть")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())