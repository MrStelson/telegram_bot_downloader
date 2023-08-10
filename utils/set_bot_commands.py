from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Вывести справку"),
            types.BotCommand("audio", "Скачать аудио из ютуба"),
            types.BotCommand("video", "Скачать видео из ютуба"),
        ]
    )
