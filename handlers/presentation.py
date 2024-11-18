from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message
from states.state import InitPresentation
from aiogram.fsm.context import FSMContext
router = Router()


@router.message(Command('create_presentation'))
async def cmd_create_presentation (message: Message, state: FSMContext):
    await message.answer('Напишите промпт для создания презентации')
    await state.set_state(InitPresentation.text)

@router.message(InitPresentation.text)
async def cmd_handler_presentaion(message: Message, state: FSMContext):
    text = message.text.lower()
    await message.reply(f"Генерирую презентацию по теме: {topic}...")

    # Вызываем функцию для создания презентации
    pptx_file = await create_presentation(topic)

    if pptx_file:
        # Отправляем файл пользователю
        await message.answer_document(open(pptx_file, 'rb'))
    else:
        await message.reply("К сожалению, не удалось создать презентацию. Попробуйте позже.")
