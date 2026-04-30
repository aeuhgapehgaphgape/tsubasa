import asyncio
from aiogram import Bot, Dispatcher

# ================== CONFIG ==================
TOKEN = "8711733093:AAGk2YUkXTpmRxwXsKiRR9dOQGViX2hzvko"
CHAT_ID = -1003857846789  # твой канал/группа

PHOTO = "https://img3.akspic.ru/attachments/crops/9/1/0/6/7/176019/176019-kirishima_touka-ken_kaneki-anime-tokijskij_gul-rize_kamishiro-1920x1080.jpg"

TEXT = (
    "⚠️ УВЕДОМЛЕНИЕ\n\n"
    "• Соблюдайте правила\n"
    "• Без спама\n"
    "• Инфо: @AdapterTbs"
)

# ================== BOT ==================
bot = Bot(token=TOKEN)
dp = Dispatcher()

# ================== LOOP ==================
async def send_loop():
    while True:
        try:
            await bot.send_photo(
                chat_id=CHAT_ID,
                photo=PHOTO,
                caption=TEXT
            )
            print("✔ Отправлено")
        except Exception as e:
            print("Ошибка:", e)

        await asyncio.sleep(900)  # 15 минут

# ================== START ==================
async def main():
    asyncio.create_task(send_loop())
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
