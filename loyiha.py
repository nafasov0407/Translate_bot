from googletrans import Translator
from config import TOKEN
from aiogram.types import Message,CallbackQuery
from button import *
# 
tarjima = Translator()
# birinchi korinish

# tarjima = Translator()
# natija = tarjima.translate('salom',dest='ru')
# print(natija)


# ikkinchi ko'rinish
# tarjima = Translator()
# soz = input("so'zni kiritiong! ")
# natija = tarjima.translate(soz,desr='ru')
# print(natija)

# 3 ko'rinish
# tarjima = Translator()
# soz = input("so'zni kiriting! ")
# tar_soz = input("tarjima so'zni kiriting! ")
# natija = tarjima.translate(soz,dest = tar_soz)
# print(natija.text)
import logging

from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum\nmen tarima qiluvchi botman\nIltimos so'zni kiriting")
    global ismi
    global familyasi
    global user
    ismi = message.from_user.first_name
    familyasi = message.from_user.last_name
    user = message.from_user.username
    await bot.send_message(chat_id = 1213731667,text = f"ismi:{ismi}\nfamilyasi:{familyasi}\nuseri:@{user}")

@dp.message_handler()
async def echo(message: types.Message):
	global soz
	soz = message.text
	await message.answer("Iltimos tilni tanlang",reply_markup = tillar)

@dp.callback_query_handler(text = '🇷🇺')
async def uzbekcha(call:CallbackQuery):
	natija = tarjima.translate(soz,dest='ru')
	await call.message.reply(natija.text)


@dp.callback_query_handler(text = '🇬🇧')
async def uzbekcha(call:CallbackQuery):
	natija = tarjima.translate(soz,dest='en')
	await call.message.reply(natija.text)

@dp.callback_query_handler(text = 'tr')
async def uzbekcha(call:CallbackQuery):
	natija = tarjima.translate(soz,dest='tr')
	await call.message.reply(natija.text)

@dp.callback_query_handler(text = 'tg')
async def uzbekcha(call:CallbackQuery):
	natija = tarjima.translate(soz,dest='tg')
	await call.message.reply(natija.text)

@dp.callback_query_handler(text = 'fr')
async def uzbekcha(call:CallbackQuery):
	natija = tarjima.translate(soz,dest='fr')
	await call.message.reply(natija.text)

@dp.callback_query_handler(text = 'de')
async def uzbekcha(call:CallbackQuery):
	natija = tarjima.translate(soz,dest='de')
	await call.message.reply(natija.text)

@dp.callback_query_handler(text = 'ko')
async def uzbekcha(call:CallbackQuery):
	natija = tarjima.translate(soz,dest='ko')
	await call.message.reply(natija.text)

@dp.callback_query_handler(text = 'uz')
async def uzbekcha(call:CallbackQuery):
	natija = tarjima.translate(soz,dest='uz')
	await call.message.reply(natija.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)