from aiogram.dispatcher.filters.state import State, StatesGroup

class States(StatesGroup):

    work = State()
    re_start = State()
    question = State()
    image = State()