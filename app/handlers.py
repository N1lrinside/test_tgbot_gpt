from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from app.generator_message import chat_gpt
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

rt = Router()

class Generate(StatesGroup):
    text = State()
@rt.message(CommandStart())
async def main(message: Message, state: FSMContext):
    await message.answer('hi')
    await state.clear()

@rt.message(Generate.text)
async def check(message: Message):
    await message.answer('ЖДИ')
@rt.message(F.text)
async def answer(message: Message, state: FSMContext):
    await state.set_state(Generate.text)
    response = await chat_gpt(message.text)
    await message.answer(response.choices[0].message.content)
    await state.clear()