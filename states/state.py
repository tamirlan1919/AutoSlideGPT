from aiogram.fsm.state import State, StatesGroup

class InitPresentation(StatesGroup):
    text = State()