from aiogram.fsm.state import StatesGroup, State


class Buttons_text:
    hello = "Hello"
    help = "Help"
    last_day_news = "Get news for the day"
    last_hour_news = "Get news for the hour"
    add_source = "Add Source"


class FSMFillForm(StatesGroup):
    fill_url = State()  # Состояние ожидания ввода url
