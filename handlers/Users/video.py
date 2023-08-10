from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command

from loader import dp, bot
from states.Download import DownloadVideo

from pytube import YouTube
import os
import uuid


def download_video(url):
    video_id = uuid.uuid4().fields[-1]
    yt = YouTube(url)
    yt.streams.filter(progressive=True).desc().first().download("video", f"{video_id}.mp4")
    return f"{video_id}.mp4"


@dp.message_handler(Command('video'))
async def bot_start_dow_video(message: types.Message):
    print('Start_dowload_video')
    await message.answer(text=f"Привет, {message.from_user.full_name}, скинь ссылку на видео")
    await DownloadVideo.download.set()


@dp.message_handler(state=DownloadVideo.download)
async def bot_dowload_video(message: types.Message, state: FSMContext):
    print('Downloading video...')
    await message.answer(text="Начинаю скачивание")
    title = download_video(message.text)
    video = open(f'video/{title}', 'rb')
    await message.answer(text="Все скачалось держи видео")
    try:
        await bot.send_video(message.chat.id, video)
        # await bot.send_message(message.chat.id, text='')
    except Exception as e:
        await message.answer(text=f"{e}")
    os.remove(f'video/{title}')
    await state.finish()
