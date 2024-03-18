import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import F

TOKEN = "6779295155:AAH8Iq5yGkUHVoG-r-DgkSgr9JI9eUOB35M"
dp = Dispatcher()

@dp.message(CommandStart())
async def starting(message: Message):
    await message.answer(text="Assalomu alaykum! Bu bot siz nima yuborganligingizni aniqlab beradi!")

@dp.message(F.text)
async def start_handler(message: Message):
    user = message.from_user.full_name
    await message.answer(text=f"{user} siz tekst yubordingiz")

@dp.message(F.dice)
async def send_dice(message:Message):
    user = message.from_user.full_name
    dice = message.dice.emoji
    await message.answer(text=f"{user} siz dice emoji yubordingiz")

@dp.message(F.video)
async def send_video(message: Message):
    user = message.from_user.full_name
    video = message.video
    await message.answer(text=f"{user} siz video yubordingiz")
    
@dp.message(F.photo)
async def send_photo(message: Message):
    user = message.from_user.full_name
    photo = message.photo
    await message.answer(text=f"{user} siz foto yubordingiz")

@dp.message(F.contact)
async def send_contact(message: Message):
    user = message.from_user.full_name
    contact = message.contact
    await message.answer(text=f"{user} siz kontakt yubordingiz")
    
@dp.message(F.game)
async def send_game(message: Message):
    user = message.from_user.full_name
    game = message.game
    await message.answer(text=f"{user} siz o'yin yubordingiz")
    
@dp.message(F.poll)
async def send_poll(message: Message):
    user = message.from_user.full_name
    poll = message.poll
    await message.answer(text=f"{user} siz poll yubordingiz")
    
@dp.message(F.location)
async def send_location(message: Message):
    user = message.from_user.full_name
    location = message.location
    await message.answer(text=f"{user} siz lokatsiya yubordingiz")
    
@dp.message(F.sticker)
async def send_sticker(message: Message):
    user = message.from_user.full_name
    sticker = message.sticker
    await message.answer(text=f"{user} siz stiker yubordingiz")

@dp.message(F.animation)
async def send_animation(message: Message):
    user = message.from_user.full_name
    animation = message.animation
    await message.answer(text=f"{user} siz animatsiya yubordingiz")
    
@dp.message(F.document)
async def send_document(message: Message):
    user = message.from_user.full_name
    document = message.document
    await message.answer(text=f"{user} siz dokument yubordingiz")
    
@dp.message(F.audio)
async def send_audio(message: Message):
    user = message.from_user.full_name
    mp3 = message.audio
    await message.answer(text=f"{user} siz audio yubordingiz")

async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())