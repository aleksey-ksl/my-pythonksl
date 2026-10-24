from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
import asyncio
import json
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import CallbackQuery
from pathlib import Path
def get_filename(user_id: int):
    return Path(__file__).resolve().parent / f"cash-{user_id}.json"


TOKEN = "ТВОЙ_ТОКЕН_ТУТ"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message : Message):
    btn_add = InlineKeyboardButton(text="Добавить трату", callback_data="menu_add")
    btn_total = InlineKeyboardButton(text="Мои траты", callback_data="menu_total")
    btn_delete = InlineKeyboardButton(text="Удалить все", callback_data="menu_delete")
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[btn_add],
                                                     [btn_total],
                                                     [btn_delete]
                                                     ])
    await message.answer("Привет! Я твой бот-кошелек. \n Выбери действие в меню ниже:", reply_markup=keyboard)

@dp.callback_query(F.data == "menu_add")
async def process_menu_add(call: CallbackQuery):
    await call.answer()
    await call.message.answer("Напиши мне сообщение в формет: Название Сумма\nНапример: Кофе 500")
@dp.callback_query(F.data == "menu_total")
async def process_menu_total(call: CallbackQuery):
    await call.answer()
    await total(call.message, call.from_user.id)


@dp.callback_query(F.data == "menu_delete")
async def process_menu_delete(call: CallbackQuery):
    await call.answer()
    await delete(call.message, call.from_user.id)

@dp.message(F.text & ~F.text.startswith("/"))
async def cash(message: Message):
    user_id = message.from_user.id
    filename = get_filename(user_id)

    text = message.text.strip()
    parts = text.rsplit(maxsplit=1)

    if len(parts) != 2:
        await message.answer(
            "Неверный формат!\nПример: Кофе 500"
        )
        return

    name = parts[0]

    try:
        summa = int(parts[1])
        if summa <= 0:
            await message.answer("Сумма должна быть больше нуля!")
            return
    except ValueError:
        await message.answer(
            "Сумма должна быть числом!\nПример: Кофе 500"
        )
        return

    try:
        with open(filename, "r", encoding="utf-8") as file:
            rashod = json.load(file)
            if not isinstance(rashod, list):
                rashod = []
    except (FileNotFoundError, json.JSONDecodeError):
        rashod = []

    rashod.append({
        "Название": name,
        "Сумма": summa
    })

    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(rashod, file, ensure_ascii=False, indent=4)
    except OSError as e:
        print(f"Ошибка записи файла: {e}")
        await message.answer("Не удалось сохранить расход!")
        return

    await message.answer(f"Записал: {name} — {summa} ₽")
    print("ID пользователя:", message.from_user.id)
    print("Путь сохранения:", filename.resolve())
    print("Файл сохранён:", filename)
    print("Содержимое:", rashod)
@dp.message(Command("total"))
async def total(message: Message, user_id=None):
    if user_id is None:
        user_id = message.from_user.id
    filename = get_filename(user_id)
    print("Читаю файл:", filename)
    print("Файл существует:", filename.exists())
    try:
        with open(filename, "r", encoding="utf-8") as file:
            rashod = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        await message.answer("Расходов пока нет!")
        return

    if not rashod:
        await message.answer("Расходов пока нет!")
        return

    itog = sum(r["Сумма"] for r in rashod)

    lines = "\n".join(
        f"{r['Название']} - {r['Сумма']}Р"
        for r in rashod
    )

    await message.answer(f"{lines}\nВсего: {itog}Р")
@dp.message(Command("delete"))
async def delete(message: Message, user_id=None):
    if user_id is None:
        user_id = message.from_user.id
    filename = get_filename(user_id)
    with open(filename, "w", encoding="utf-8") as file:
        json.dump([], file)
        await message.answer("Список удален!")










async def main():
    print("Bot started")
    await dp.start_polling(bot)
asyncio.run(main())