import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor

# Замените на свой токен бота
TOKEN = "7954022473:AAH6VAnn0I2yC5wEuQbc4Al7zJfCMw_iWsk"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Включаем логирование
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=['start'])
async def start_command(message: Message):
    await message.answer("👋 Привет! Отправь мне свой номер для голосования.")

@dp.message_handler(content_types=types.ContentType.CONTACT)
async def register_vote(message: Message):
    phone_number = message.contact.phone_number
    user_id = message.from_user.id

    # Здесь можно добавить голосование, например, отправить номер в нужный сервис

    await message.answer(f"✅ Твой номер {phone_number} зарегистрирован для голосования!")
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
