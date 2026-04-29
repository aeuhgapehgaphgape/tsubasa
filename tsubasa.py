import asyncio
from aiogram import Bot, Dispatcher

# ================== НАСТРОЙКИ ==================
TOKEN = "8711733093:AAGdVXBSqDWMeTsRAUIamZa_hXaFwYQs3so"
CHAT_ID = -1003284226593 # ID чата / канала

PHOTO = "https://img3.akspic.ru/attachments/crops/9/1/0/6/7/176019/176019-kirishima_touka-ken_kaneki-anime-tokijskij_gul-rize_kamishiro-1920x1080.jpg"

TEXT = (
    "⚠️ УВЕДОМЛЕНИЕ ДЛЯ УЧАСТНИКОВ\n\n"
    "Во избежание блокировок, просим вас придерживаться правил сообщества:\n\n"
    "• Соблюдайте порядок: Флуд и провокации недопустимы.\n\n"
    "• Уважайте коллег: Оскорбления караются баном.\n\n"
    "• Инфо-канал: @AdapterTbs\n\n"
    "Благодарим за соблюдение регламента."
)

# ================== БОТ ==================
bot = Bot(token=TOKEN)
dp = Dispatcher()

async def spam_loop():
    while True:
        try:
            await bot.send_photo(
                chat_id=CHAT_ID,
                photo=PHOTO,
                caption=TEXT
            )
        except Exception as e:
            print("Ошибка отправки:", e)

        await asyncio.sleep(900)  # 15 минут

async def main():
    asyncio.create_task(spam_loop())
    await dp.start_polling(bot)

if name == "__main__":
    asyncio.run(main())
