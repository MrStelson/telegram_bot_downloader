from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command

from loader import dp, bot
from states.Download import DownloadAudio

from pytube import YouTube
import os
import uuid


def download_audio(url):
    audio_id = uuid.uuid4().fields[-1]
    yt = YouTube(url)
    yt.streams.filter(only_audio=True).first().download("audio", f"{audio_id}.mp3")
    return f"{audio_id}.mp3"


@dp.message_handler(Command('audio'))
async def bot_start_dow_audio(message: types.Message):
    print('Start_dowload_audio')
    await message.answer(
        text=f"Привет, {message.from_user.full_name}, скинь ссылку на видео и я отправлю ее тебе ввиде аудио."
    )
    await DownloadAudio.download.set()


@dp.message_handler(state=DownloadAudio.download)
async def bot_dowload_audio(message: types.Message, state: FSMContext):
    print('Downloading audio...')
    await message.answer(text="Начинаю скачивание")
    title = download_audio(message.text)
    audio = open(f'audio/{title}', 'rb')
    await message.answer(text="Все скачалось держи аудио")
    try:
        await bot.send_audio(message.chat.id, audio)
        # await bot.send_message(message.chat.id, text='')
    except Exception as e:
        await message.answer(text=f"{e}")
    os.remove(f'audio/{title}')
    await state.finish()
