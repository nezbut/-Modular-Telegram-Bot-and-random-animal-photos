from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon_ru import LEXIXON_RU

router = Router()

@router.message()
async def other_message(message: Message):
    try:
        await message.send_copy(message.chat.id)
    except Exception:
        await message.answer(LEXIXON_RU['no_copy'])

__all__ = (
    'router',
)