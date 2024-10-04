from aiogram.fsm.state import StatesGroup, State


class Buttons_text:
    hello = "Hello"
    help = "Help"
    last_day_news = "Get_news_for_the_day"
    last_hour_news = "Get_news_for_the_hour"
    add_source = "Add_Source"


class FSMFillForm(StatesGroup):
    fill_url = State()  # Состояние ожидания ввода url
