from aiogram import Router, types, F
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

router = Router()

class Dialog(StatesGroup):
    waiting_for_choice = State()

BUTTONS = ["Школьная программа", "Формулы", "Прочее"]

async def get_keyboard():
    start_keyboard = ReplyKeyboardMarkup(
        keyboard = [
            [
                KeyboardButton(text = "Школьная программа"),
                KeyboardButton(text = "Формулы"),
                KeyboardButton(text = "Прочее")
            ]
        ],
        resize_keyboard = True,
        one_time_keyboard = True
    )
    return start_keyboard

@router.callback_query(F.data == "main_menu")
async def go_to_menu(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.message.delete()
    await callback.message.answer(
        "🎋 Вы завершили путь и вернулись к каменному фонарю...",
        reply_markup = await get_keyboard()
    )
    await state.set_state(Dialog.waiting_for_choice)

@router.message(Command(commands = ['start', 'menu']))
async def cmd_start(message: types.Message, state: FSMContext) -> None:
    await message.answer(
    text="<i>🌸 Ветер приносит цифры и формулы...</i>\n"
         "<b>Добро пожаловать в сад математики Mugen Tei</b>\n"
         "<i>Выберите тропинку для прогулки:</i>",
        parse_mode="HTML",
        reply_markup = await get_keyboard()
    )
    await state.set_state(Dialog.waiting_for_choice)

@router.message()
async def other_message(message: types.Message, state: FSMContext):
    await message.answer(
        "🌸 Лепесток сбился с ветра \n"
        "<i> Позовите новый поток командой /start</i>",
        reply_markup = ReplyKeyboardRemove(),
        parse_mode = "HTML"
    )
    await state.clear()
    
