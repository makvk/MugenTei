from aiogram import Router, types, F
from aiogram.types import CallbackQuery, FSInputFile

router = Router()

@router.callback_query(F.data.startswith("fig"))
async def formulas_fig1(callback_query: types.CallbackQuery):
    await callback_query.answer() 
    pic_name = callback_query.data[3:7]
    pic_number = callback_query.data[7:]
    image_from_pc = FSInputFile(rf".\pictures\pic{pic_name}{pic_number}_1.png")
    await callback_query.message.answer_photo(
        image_from_pc
    )


