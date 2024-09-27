import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from aiogram.types import ContentType
from config import API_TOKEN
from handlers import handle_photos

log_directory = "logs"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    filename=os.path.join(log_directory, "bot.log"),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Регистрация хендлера для обработки фото
dp.register_message_handler(handle_photos, content_types=ContentType.PHOTO)

# Функция для запуска бота
def main():
    executor.start_polling(dp, skip_updates=True)

if __name__ == '__main__':
    main()