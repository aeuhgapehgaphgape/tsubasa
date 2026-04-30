import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# ================== CONFIG ==================
TOKEN = "8711733093:AAFW6v-A_RysewWfpsOqIDZVEztU3Bf1Fxs"
CHAT_ID = -1003857846789

PHOTO = "https://img3.akspic.ru/crops/5/2/7/5/1/115725/115725-animacionnoe_muzykalnoe_video-ken_kaneki-vurdalak-anime-tokio_vurdalak-1920x1080.jpg"

# ================== ТЕКСТЫ ==================
MAIN_TEXT = (
    "⚠️ УВЕДОМЛЕНИЕ ДЛЯ УЧАСТНИКОВ\n\n"
    "Во избежание блокировок, просим вас придерживаться правил сообщества:\n\n"
    "• Соблюдайте порядок: Флуд и провокации недопустимы.\n\n"
    "• Уважайте коллег: Оскорбления караются баном.\n\n"
    "• Инфо-канал: @AdapterTbs\n\n"
    "Благодарим за соблюдение регламента"
)

START_TEXT = (
    "^ Owner - @Teddam\n\n"
    "^ Chat - @AdapterTBS"
)

# ================== BOT ==================
bot = Bot(token=TOKEN)
dp = Dispatcher()

# ================== /start ==================
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(START_TEXT)

# ================== СПАМ ЦИКЛ ==================
async def spam_loop():
    while True:
        try:
            await bot.send_photo(
                chat_id=CHAT_ID,
                photo=PHOTO,
                caption=MAIN_TEXT
            )
            print("✔ Отправлено")
        except Exception as e:
            print("Ошибка:", e)

        await asyncio.sleep(900)  # 15 минут

# ================== START ==================
async def main():
    asyncio.create_task(spam_loop())
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
