from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup

tillar = InlineKeyboardMarkup(
	inline_keyboard = [
		[
				InlineKeyboardButton(text = " 🇷🇺 Rus",callback_data = '🇷🇺'),InlineKeyboardButton(text = " 🇬🇧 Eng",callback_data = '🇬🇧'),InlineKeyboardButton(text = "🇹🇷 turkish",callback_data = 'tr'),InlineKeyboardButton(text = " 🇹🇯 tajik",callback_data = 'tg')
		],
		[
				InlineKeyboardButton(text = "🇫🇷 french",callback_data = 'fr'),InlineKeyboardButton(text = "🇩🇪 german",callback_data = 'de'),InlineKeyboardButton(text = "🇰🇷 korean",callback_data = 'ko'),InlineKeyboardButton(text = " uzbek",callback_data = 'uz')
		],
	],
)