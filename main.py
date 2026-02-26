from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# ID твоего канала (начинается с -100...)
CHANNEL_ID = -1002802431441  # Замени на ID своего канала
BOT_TOKEN = "8763384742:AAEvecBkBiz6HnudrWLQhk2huXmd-Bz4SQs"  # Замени на токен своего бота

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    # Проверяем статус пользователя в канале
    user_channel_status = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)
    
    if user_channel_status.status not in ['left', 'kicked']:
        await message.answer("🎉 Добро пожаловать в бот! 🎉")
        await message.answer("Этот бот предназначен для арбитража трафика. После подписки вы получаете доступ к премиум ботам.")
        kb_bots = [
            [types.InlineKeyboardButton(text="@eafbuniqbot", url="https://t.me/eafbuniqbot")],
            [types.InlineKeyboardButton(text="@eafbmailbot", url="https://t.me/eafbmailbot")],
            [types.InlineKeyboardButton(text="@eafbbot", url="https://t.me/eafbbot")],
        ]
        keyboard_bots = types.InlineKeyboardMarkup(inline_keyboard=kb_bots)
        await message.answer("Доступные боты:", reply_markup=keyboard_bots)
    else:
        # Создаем кнопки
        kb = [
            [types.InlineKeyboardButton(text="Подписаться на канал", url="https://t.me/ebarbitrage")],  # Замени на ссылку своего канала
            [types.InlineKeyboardButton(text="Проверить", callback_data="check_sub")]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
        await message.answer("Для доступа к боту подпишитесь на канал:", reply_markup=keyboard)

# Обработка нажатия на кнопку "Проверить"
@dp.callback_query(lambda c: c.data == "check_sub")
async def check_callback(callback: types.CallbackQuery):
    status = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=callback.from_user.id)
    if status.status not in ['left', 'kicked']:
        await callback.message.edit_text("🎉 Спасибо за подписку! Теперь бот полностью доступен. 🎉")
        await callback.message.answer("Этот бот предназначен для арбитража трафика. После подписки вы получаете доступ к премиум ботам.")
        kb_bots = [
            [types.InlineKeyboardButton(text="@eafbuniqbot", url="https://t.me/eafbuniqbot")],
            [types.InlineKeyboardButton(text="@eafbmailbot", url="https://t.me/eafbmailbot")],
            [types.InlineKeyboardButton(text="@eafbbot", url="https://t.me/eafbbot")],
        ]
        keyboard_bots = types.InlineKeyboardMarkup(inline_keyboard=kb_bots)
        await callback.message.answer("Доступные боты:", reply_markup=keyboard_bots)
    else:
        await callback.answer("Вы всё еще не подписаны!", show_alert=True)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())