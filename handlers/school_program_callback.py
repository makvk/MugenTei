from aiogram import Router, types, F
from aiogram.types import CallbackQuery

router = Router()

@router.callback_query(F.data.startswith("class"))
async def commands_sch(callback: CallbackQuery):
    await callback.answer(
        "🎐 Раздел временно закрыт бумажным экраном. Мастера работают над обновлением...",
    )