from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/help - Получить справку",
            "/video - Это команда для скачивания видео",
            "/audio - Это команда для скачивания видео и отправка вам аудио сообщением"
            )

    await message.answer("\n".join(text))