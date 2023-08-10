from aiogram.dispatcher.filters.state import StatesGroup, State


class DownloadVideo(StatesGroup):
    download = State()

class DownloadAudio(StatesGroup):
    download = State()

