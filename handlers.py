import logging
from aiogram import types
from config import DESTINATION_CHAT_ID


async def handle_photos(message: types.Message):
    # Проверяем, что сообщение не из destination group, чтобы избежать циклической пересылки
    if message.chat.id == DESTINATION_CHAT_ID:
        logging.info("Сообщение из destination group. Пропускаем.")
        return

    if message.photo:
        # Получаем самое большое фото (наивысшее разрешение)
        largest_photo = message.photo[-1].file_id

        # Отправляем фото в общий чат без подписи
        try:
            await message.bot.send_photo(
                chat_id=DESTINATION_CHAT_ID,
                photo=largest_photo
                
            )
            logging.info(f"Фото отправлено из чата {message.chat.id} в {DESTINATION_CHAT_ID}")
        except Exception as e:
            logging.error(f"Ошибка при отправке фото: {e}")
    else:
        logging.info(f"Сообщение из чата {message.chat.id} не содержит фото.")