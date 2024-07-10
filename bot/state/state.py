from aiogram.fsm.state import StatesGroup, State


class StepState(StatesGroup):
    step1 = State()
    step2 = State()
    step3 = State()
    step4 = State()


class BackState(StatesGroup):
    back1 = State()
