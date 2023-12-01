from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from API_animals_photos.class_random_animals import RandomPhotoAnimalAPI
from lexicon.lexicon_ru import LEXIXON_RU
import logging

router = Router()
random_animals_photos = RandomPhotoAnimalAPI()


@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(LEXIXON_RU['start'])

@router.message(Command(commands=['help']))
async def help_command(message: Message):
    await message.answer(LEXIXON_RU['help'])

@router.message(Command(commands=['cats', 'dogs', 'foxs']))
async def get_random_animals_photo(message: Message):
    animal = message.text.lower().strip()
    animal_photo_link = await random_animals_photos.request(animal)
    try:
        await message.answer_photo(animal_photo_link)
    except Exception as e:
        logging.error(e)
        await message.answer(LEXIXON_RU['bad_request'])

__all__ = (
    'router',
)