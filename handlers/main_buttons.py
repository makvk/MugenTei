from aiogram import Router, types, F
from aiogram.types import ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.fsm.context import FSMContext
from handlers.common import Dialog, BUTTONS
from aiogram.filters.callback_data import CallbackData
from typing import Optional

router = Router()

PL_FIGURES = [
    "1. <b>Треугольник</b> — <i>Вершина Фудзи</i>",
    "2. <b>Прямоугольник</b> — <i>Свиток мудрости</i>",
    "3. <b>Квадрат</b> — <i>Печать императора</i>",
    "4. <b>Параллелограмм</b> — <i>Падающий водопад</i>",
    "5. <b>Ромб</b> — <i>Крылья журавля</i>",
    "6. <b>Трапеция</b> — <i>Храмовая крыша</i>",
    "7. <b>Круг</b> — <i>Луна в пруду</i>",
    "8. <b>Эллипс</b> — <i>Глаз Будды</i>",
    "9. <b>Сектор круга</b> — <i>Веер гейши</i>",
    "10. <b>Сегмент круга</b> — <i>Мост в облаках</i>",
    "11. <b>Выпуклый четырехугольник</b> — <i>Боевой щит</i>",
    "12. <b>Правильный многоугольник</b> — <i>Соты мудреца</i>"
]

ST_FIGURES = [
    "1. <b>Куб</b> — <i>Сокровищница самурая</i>",
    "2. <b>Параллелепипед</b> — <i>Каменный мост</i>",  
    "3. <b>Призма</b> — <i>Храмовая колонна</i>",
    "4. <b>Пирамида</b> — <i>Путь к просветлению</i>",
    "5. <b>Правильный тетраэдр</b> — <i>Священная гора</i>",
    
    "6. <b>Цилиндр</b> — <i>Бамбуковый свиток</i>",
    "7. <b>Конус</b> — <i>Шляпа монаха</i>",
    "8. <b>Усечённый конус</b> — <i>Чайная чаша</i>", 
    "9. <b>Шар</b> — <i>Лунный свет</i>",
    "10. <b>Шаровой сегмент</b> — <i>Раковина жемчужины</i>",
    "11. <b>Шаровой слой</b> — <i>Кольцо дракона</i>",

    "12. <b>Эллипсоид</b> — <i>Глаз всевидящего</i>"
]

async def get_kb_0():
    keyboard = [
        [
            InlineKeyboardButton(text = "5", callback_data = "class5"),
            InlineKeyboardButton(text = "6", callback_data = "class6"),
            InlineKeyboardButton(text = "7", callback_data = "class7")
        ],
        [
            InlineKeyboardButton(text = "8", callback_data = "class8"),
            InlineKeyboardButton(text = "9", callback_data = "class9"),
            InlineKeyboardButton(text = "10", callback_data = "class10")
        ],
        [
            InlineKeyboardButton(text = "11", callback_data = "class11"),
            InlineKeyboardButton(text = "ОГЭ", callback_data = "classEX9"),
            InlineKeyboardButton(text = "ЕГЭ", callback_data = "classEX11")
        ],
        [
            InlineKeyboardButton(text = "Меню", callback_data = "main_menu"),
        ]
    ]
    return keyboard

async def get_kb_10():
    keyboard = [
        [
            InlineKeyboardButton(text = "Планиметрия", callback_data = "formulas_pl"),
            InlineKeyboardButton(text = "Стереометрия", callback_data = "formulas_st")
        ],
        [
            InlineKeyboardButton(text = "Меню", callback_data = "main_menu"),
        ]
    ]
    return keyboard

async def get_kb_100():
    keyboard = [
        [
            InlineKeyboardButton(text = "1", callback_data = "fig_pl_1"),
            InlineKeyboardButton(text = "2", callback_data = "fig_pl_2"),
            InlineKeyboardButton(text = "3", callback_data = "fig_pl_3"),
        ],
        [
            InlineKeyboardButton(text = "4", callback_data = "fig_pl_4"),
            InlineKeyboardButton(text = "5", callback_data = "fig_pl_5"),
            InlineKeyboardButton(text = "6", callback_data = "fig_pl_6"),
        ],
        [
            InlineKeyboardButton(text = "7", callback_data = "fig_pl_7"),
            InlineKeyboardButton(text = "8", callback_data = "fig_pl_8"),
            InlineKeyboardButton(text = "9", callback_data = "fig_pl_9"),
        ],
        [
            InlineKeyboardButton(text = "10", callback_data = "fig_pl_10"),
            InlineKeyboardButton(text = "11", callback_data = "fig_pl_11"),
            InlineKeyboardButton(text = "12", callback_data = "fig_pl_12"),
        ],
        [
            InlineKeyboardButton(text = "Меню", callback_data = "main_menu"),
            InlineKeyboardButton(text = "Назад", callback_data = "formulas_back"),
        ]
    ]
    return keyboard

async def get_kb_101():
    keyboard = [
        [
            InlineKeyboardButton(text = "1", callback_data = "fig_st_1"),
            InlineKeyboardButton(text = "2", callback_data = "fig_st_2"),
            InlineKeyboardButton(text = "3", callback_data = "fig_st_3"),
        ],
        [
            InlineKeyboardButton(text = "4", callback_data = "fig_st_4"),
            InlineKeyboardButton(text = "5", callback_data = "fig_st_5"),
            InlineKeyboardButton(text = "6", callback_data = "fig_st_6"),
        ],
        [
            InlineKeyboardButton(text = "7", callback_data = "fig_st_7"),
            InlineKeyboardButton(text = "8", callback_data = "fig_st_8"),
            InlineKeyboardButton(text = "9", callback_data = "fig_st_9"),
        ],
        [
            InlineKeyboardButton(text = "10", callback_data = "fig_st_10"),
            InlineKeyboardButton(text = "11", callback_data = "fig_st_11"),
            InlineKeyboardButton(text = "12", callback_data = "fig_st_12"),
        ],
        [
            InlineKeyboardButton(text = "Меню", callback_data = "main_menu"),
            InlineKeyboardButton(text = "Назад", callback_data = "formulas_back"),
        ]
    ]
    return keyboard

@router.message(Dialog.waiting_for_choice, F.text.in_(BUTTONS))
async def get_choice(message: types.Message, state: FSMContext):
    await message.answer(
        f"🍂 Ветер уносит ваш выбор «{message.text}» в сад познания... Приготовьтесь к чуду чисел.",
        reply_markup = ReplyKeyboardRemove()
    )
    await state.clear()
    match (message.text):
        case "Школьная программа":
            await school_program(message)
        case "Формулы":
            await message.answer(
                "🌸 Какой путь математики вам открыть сегодня?",
                reply_markup = InlineKeyboardMarkup(inline_keyboard = await get_kb_10())
            )
        case "Прочее":
            await message.answer(
                "🎐 Раздел временно закрыт бумажным экраном. Мастера работают над обновлением...",
                reply_markup = InlineKeyboardMarkup(inline_keyboard = [[InlineKeyboardButton(text = "Меню", callback_data = "main_menu")]])
            )

# Обработчик школьной программы
async def school_program(message: types.Message):
    await message.answer(
        text="🏯 <b>武道の道を選べ</b> (Выбери путь воина знаний)\n\n"
             
             "▫️ <b>5-7 классы</b> <i>• 弟子 (でし — ученик)</i> 🌱\n"
             "   Изучаем иероглифы чисел и счёт на абаке, как юные самураи\n\n"
             
             "▫️ <b>8-10 классы</b> <i>• 見習い (みならい — подмастерье)</i> ⚔️\n"
             "   Отрабатываем удары алгебры и парируем атаки геометрии\n\n"
             
             "▫️ <b>11 класс</b> <i>• 武士 (ぶし — воин)</i> 🎭\n"
             "   Сражаемся с демонами тригонометрии и логарифмов\n\n"
             
             "▫️ <b>ОГЭ / ЕГЭ</b> <i>• 試練 (しれん — испытание)</i> 🏮\n"
             "   Последний бой перед вступлением в клан мудрецов\n\n"
             
             "<i>«七転び八起き»</i> — падай семь раз, поднимайся восемь!\n"
             "<b>頑張って!</b> 🎋",
             
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=await get_kb_0()),
    )

@router.callback_query(F.data.in_(["formulas_pl", "formulas_st"]))
async def formulas(callback: types.CallbackQuery):
    match(callback.data):
        case "formulas_pl":
            await callback.message.edit_text(
                f"🌸 <b>Выберите путь среди цветущих фигур:</b>\n\n"
                f"{'\n'.join(PL_FIGURES)}",
                parse_mode = "HTML",
                reply_markup = InlineKeyboardMarkup(inline_keyboard = await get_kb_100())
            )
            await callback.answer()
        case "formulas_st":
            await callback.message.edit_text(
                f"🌸 <b>Выберите путь среди цветущих фигур:</b>\n\n"
                f"{'\n'.join(ST_FIGURES)}",
                parse_mode = "HTML",
                reply_markup = InlineKeyboardMarkup(inline_keyboard = await get_kb_101())
            )
            await callback.answer()

@router.callback_query(F.data == "formulas_back")
async def back_to_formulas_menu(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "🌸 Какой путь математики вам открыть сегодня?",
        reply_markup = InlineKeyboardMarkup(inline_keyboard = await get_kb_10())
    )
    await callback.answer()