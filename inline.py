from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

cd = CallbackData("Inline","action")

def getInline() -> InlineKeyboardMarkup:
	Inline = InlineKeyboardMarkup(row_width = 2,inline_keyboard = [
		[InlineKeyboardButton("Каталог",callback_data = cd.new("Каталог"))],
		[InlineKeyboardButton("Для заказа",callback_data = cd.new("click-2")),InlineKeyboardButton("Помощь",callback_data = cd.new("help"))],
		[InlineKeyboardButton("Партнерам",callback_data = cd.new("partner"))],
		[InlineKeyboardButton("Опубликовать товар",callback_data = cd.new("click-5"))]
	])

	return Inline

def getInline2() -> InlineKeyboardMarkup:
	Inline = InlineKeyboardMarkup(row_width = 2,inline_keyboard = [
		[InlineKeyboardButton("Получить портнерскую ссылку",callback_data = cd.new("click-1"))],
		[InlineKeyboardButton("Мои баллы",callback_data = cd.new("count"))],
		[InlineKeyboardButton("Запросить скидку",callback_data = cd.new("discount")),InlineKeyboardButton("Поделиться",callback_data = cd.new("Поделиться"))],
		[InlineKeyboardButton("Назад",callback_data = cd.new("click-5"))]
	])

	return Inline

def getInline3() -> InlineKeyboardMarkup:
	Inline = InlineKeyboardMarkup(inline_keyboard = [
		[InlineKeyboardButton("Рассказать друзьям VK","https://vk.com/english_russian_language_exchang")],
		[InlineKeyboardButton("Рассказать друзьям Telegam","https://web.telegram.org/k/")],
		[InlineKeyboardButton("Рассказать друзьям Facebook","https://ru-ru.facebook.com/")],
		[InlineKeyboardButton("Рассказать друзьям Twitter","https://twitter.com/?lang=ru")],
		[InlineKeyboardButton("Назад",callback_data = cd.new('VK'))]
	])

	return Inline

def getInline4() -> InlineKeyboardMarkup:
	Inline = InlineKeyboardMarkup(inline_keyboard = [
		[InlineKeyboardButton("Женская",callback_data = cd.new('women'))],
		[InlineKeyboardButton("Мужская",callback_data = cd.new('men'))],
		[InlineKeyboardButton("Назад",callback_data = cd.new('VK'))]
	])

	return Inline
