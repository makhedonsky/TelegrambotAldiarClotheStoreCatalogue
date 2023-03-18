from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

cd = CallbackData("Inline","action")

def main_menu() -> InlineKeyboardMarkup:
	Inline = InlineKeyboardMarkup(row_width = 2,inline_keyboard = [
		[InlineKeyboardButton("Каталог",callback_data = cd.new("Каталог"))],
		[InlineKeyboardButton("Помощь",callback_data = cd.new("help")),InlineKeyboardButton("Партнерам",callback_data = cd.new("partner"))],
		[InlineKeyboardButton("Опубликовать товар",callback_data = cd.new("new_goods"))]
	])

	return Inline

def help_keyboard() -> InlineKeyboardMarkup:
	Inline = InlineKeyboardMarkup(row_width = 2,inline_keyboard = [
		[InlineKeyboardButton("Каталог",callback_data = cd.new("Каталог"))],
		[InlineKeyboardButton("Партнерам",callback_data = cd.new("partner")),InlineKeyboardButton("Опубликовать товар",callback_data = cd.new("new_goods"))],
		[InlineKeyboardButton("Назад",callback_data = cd.new("back_to_main"))]
	])

	return Inline

def partner_menu() -> InlineKeyboardMarkup:
	Inline = InlineKeyboardMarkup(row_width = 2,inline_keyboard = [
		[InlineKeyboardButton("Мои баллы",callback_data = cd.new("count"))],
		[InlineKeyboardButton("Запросить скидку",callback_data = cd.new("discount")),InlineKeyboardButton("Поделиться",callback_data = cd.new("Поделиться"))],
		[InlineKeyboardButton("Назад",callback_data = cd.new("back_to_main"))]
	])

	return Inline

def share_menu() -> InlineKeyboardMarkup:
	Inline = InlineKeyboardMarkup(inline_keyboard = [
		[InlineKeyboardButton("Рассказать друзьям VK","https://vk.com/english_russian_language_exchang")],
		[InlineKeyboardButton("Рассказать друзьям Telegam","https://web.telegram.org/k/")],
		[InlineKeyboardButton("Рассказать друзьям Facebook","https://ru-ru.facebook.com/")],
		[InlineKeyboardButton("Рассказать друзьям Twitter","https://twitter.com/?lang=ru")],
		[InlineKeyboardButton("Назад",callback_data = cd.new('bakc_to_partner'))]
	])

	return Inline

def catalog_menu() -> InlineKeyboardMarkup:
	Inline = InlineKeyboardMarkup(row_width = 2,inline_keyboard = [
		[InlineKeyboardButton("Женская",callback_data = cd.new('women'))],
		[InlineKeyboardButton("Мужская",callback_data = cd.new('men'))],
		[InlineKeyboardButton("Назад",callback_data = cd.new('back_to_main'))]
	])

	return Inline

def women_category_menu()->InlineKeyboardMarkup:
	Inline = InlineKeyboardMarkup(row_width = 2,inline_keyboard = [
		[InlineKeyboardButton("Обувь",callback_data = cd.new("women_shoes"))],
		[InlineKeyboardButton("Верхняя одежда",callback_data = cd.new("WomenOuterwear"))],
		[InlineKeyboardButton("Штаны",callback_data = cd.new("WomenPants"))],
		[InlineKeyboardButton("Аксессуары",callback_data = cd.new("WomenAccessories"))],
		[InlineKeyboardButton("Назад",callback_data = cd.new('back_to_catalog'))]
	])

	return Inline

def men_category_menu()->InlineKeyboardMarkup:
	Inline = InlineKeyboardMarkup(row_width = 2,inline_keyboard = [
		[InlineKeyboardButton("Обувь",callback_data = cd.new("men_shoes"))],
		[InlineKeyboardButton("Верхняя одежда",callback_data = cd.new("MenOuterwear"))],
		[InlineKeyboardButton("Штаны",callback_data = cd.new("MenPants"))],
		[InlineKeyboardButton("Аксессуары",callback_data = cd.new("MenAccessories"))],
		[InlineKeyboardButton("Назад",callback_data = cd.new('back_to_catalog'))]
	])

	return Inline

def women_shoes_menu() -> InlineKeyboardMarkup:
	Inline  = InlineKeyboardMarkup(row_width = 2,inline_keyboard = [	
		[InlineKeyboardButton("Кроссовки",callback_data = cd.new("women_Кроссовки") )],
		[InlineKeyboardButton("Туфли",callback_data = cd.new("women_Туфли") )],
		[InlineKeyboardButton("Сандали",callback_data = cd.new("women_Сандали") )],
		[InlineKeyboardButton("Сапоги",callback_data = cd.new("women_Сапоги") )],
		[InlineKeyboardButton("Назад",callback_data = cd.new('back_to_catalog'))]
	])

	return Inline

def men_shoes_menu() -> InlineKeyboardMarkup:
	Inline  = InlineKeyboardMarkup(row_width = 2,inline_keyboard = [	
		[InlineKeyboardButton("Кроссовки",callback_data = cd.new("men_Кроссовки"))],
		[InlineKeyboardButton("Туфли",callback_data = cd.new("men_Туфли"))],
		[InlineKeyboardButton("Сандали",callback_data = cd.new("men_Сандали"))],
		[InlineKeyboardButton("Сапоги",callback_data = cd.new("men_Сапоги"))],
		[InlineKeyboardButton("Назад",callback_data = cd.new('back_to_catalog'))]
	])

	return Inline

def women_Outerwear() -> InlineKeyboardMarkup:
	Inline = InlineKeyboardMarkup(row_width = 2,inline_keyboard = [
		[InlineKeyboardButton("Курткий", callback_data = cd.new("women_Курткий") )],
		[InlineKeyboardButton("Кофты", callback_data = cd.new("women_Кофты") )],	
		[InlineKeyboardButton("Свиторы", callback_data = cd.new("women_Свиторы"))],	
		[InlineKeyboardButton("Дождевик",callback_data = cd.new("women_Дождевик"))],
		[InlineKeyboardButton("Назад",callback_data = cd.new('women_back_to_catalog'))]	
	])

	return Inline

def men_Outerwear() -> InlineKeyboardMarkup:
	Inline = InlineKeyboardMarkup(row_width = 2,inline_keyboard = [
		[InlineKeyboardButton("Курткий", callback_data = cd.new("men_Курткий") )],
		[InlineKeyboardButton("Кофты", callback_data = cd.new("men_Кофты") )],	
		[InlineKeyboardButton("Свиторы", callback_data = cd.new("men_Свиторы"))],	
		[InlineKeyboardButton("Дождевик",callback_data = cd.new("men_Дождевик"))],
		[InlineKeyboardButton("Назад",callback_data = cd.new('men_back_to_catalog'))]
	])

	return Inline

def women_pants() -> InlineKeyboardMarkup:
	Inline = InlineKeyboardMarkup(row_width = 2,inline_keyboard = [
		[InlineKeyboardButton("Трико", callback_data = cd.new("Трико") )],
		[InlineKeyboardButton("Джинсы", callback_data = cd.new("Джинсы") )],	
		[InlineKeyboardButton("Лассины", callback_data = cd.new("Лассины"))],	
		[InlineKeyboardButton("Классический брюки",callback_data = cd.new("Классический брюки"))],
		[InlineKeyboardButton("Назад",callback_data = cd.new('back_to_catalog'))]
	])

	return Inline	

def men_pants() -> InlineKeyboardMarkup:
	Inline = InlineKeyboardMarkup(row_width = 2,inline_keyboard = [
		[InlineKeyboardButton("Трико", callback_data = cd.new("Трико") )],
		[InlineKeyboardButton("Джинсы", callback_data = cd.new("Джинсы") )],	
		[InlineKeyboardButton("Лассины", callback_data = cd.new("Лассины"))],	
		[InlineKeyboardButton("Классический брюки",callback_data = cd.new("Классический брюки"))],
		[InlineKeyboardButton("Назад",callback_data = cd.new('back_to_catalog'))]
	])

	return Inline

def Men_Accessories() -> InlineKeyboardMarkup:
	Inline = InlineKeyboardMarkup(row_width = 2,inline_keyboard = [
		[InlineKeyboardButton("Очки", callback_data = cd.new("Очки") )],
		[InlineKeyboardButton("Часы", callback_data = cd.new("Часы") )],	
		[InlineKeyboardButton("Сумки", callback_data = cd.new("Сумки"))],	
		[InlineKeyboardButton("Кальцо",callback_data = cd.new("Кальцо"))],
		[InlineKeyboardButton("Назад",callback_data = cd.new('back_to_catalog'))]
	])

	return Inline

def Women_Accessories() -> InlineKeyboardMarkup:
	Inline = InlineKeyboardMarkup(row_width = 2,inline_keyboard = [
		[InlineKeyboardButton("Очки", callback_data = cd.new("Очки") )],
		[InlineKeyboardButton("Часы", callback_data = cd.new("Часы") )],	
		[InlineKeyboardButton("Сумки", callback_data = cd.new("Сумки"))],	
		[InlineKeyboardButton("Кальцо",callback_data = cd.new("Кальцо"))],
		[InlineKeyboardButton("Назад",callback_data = cd.new('back_to_catalog'))]
	])

	return Inline

def men_women() -> InlineKeyboardMarkup:
	Inline = InlineKeyboardMarkup(row_width = 2,inline_keyboard = [
		[InlineKeyboardButton('Женская',callback_data = cd.new("Женская"))],
		[InlineKeyboardButton('Мужская',callback_data = cd.new("Мужская"))]
	])
	return Inline

def things() -> InlineKeyboardMarkup:
	Inline = InlineKeyboardMarkup(row_width = 2,inline_keyboard = [
		[InlineKeyboardButton("Предыдущий", callback_data = cd.new("Предыдущий`") )],
		[InlineKeyboardButton("Следующий", callback_data = cd.new("Следующий") )],	
		[InlineKeyboardButton("Назад", callback_data = cd.new("back_to_photo"))],	
	])

	return Inline

def category_one()->InlineKeyboardMarkup:
	Inline = InlineKeyboardMarkup(row_width = 2,inline_keyboard = [
		[InlineKeyboardButton("Обувь",callback_data = cd.new("FSM_shoes"))],
		[InlineKeyboardButton("Верхняя одежда",callback_data = cd.new("FSM_Outerwear"))],
		[InlineKeyboardButton("Штаны",callback_data = cd.new("FSM_Pants"))],
		[InlineKeyboardButton("Аксессуары",callback_data = cd.new("FSM_Accessories"))],
		[InlineKeyboardButton("Назад",callback_data = cd.new('FSM_back_to_catalog'))]
	])

	return Inline

def category_two_shoes() -> InlineKeyboardMarkup:
	Inline  = InlineKeyboardMarkup(row_width = 2,inline_keyboard = [	
		[InlineKeyboardButton("Кроссовки",callback_data = cd.new("fsm_Кроссовки"))],
		[InlineKeyboardButton("Туфли",callback_data = cd.new("fsm_Туфли"))],
		[InlineKeyboardButton("Сандали",callback_data = cd.new("fsm_Сандали"))],
		[InlineKeyboardButton("Сапоги",callback_data = cd.new("fsm_Сапоги"))],
		[InlineKeyboardButton("Назад",callback_data = cd.new('fsm_back_to_catalog'))]
	])

	return Inline

def category_two_outerwear() -> InlineKeyboardMarkup:
	Inline  = InlineKeyboardMarkup(row_width = 2,inline_keyboard = [	
		[InlineKeyboardButton("Кроссовки",callback_data = cd.new("fsm_Кроссовки"))],
		[InlineKeyboardButton("Туфли",callback_data = cd.new("fsm_Туфли"))],
		[InlineKeyboardButton("Сандали",callback_data = cd.new("fsm_Сандали"))],
		[InlineKeyboardButton("Сапоги",callback_data = cd.new("fsm_Сапоги"))],
		[InlineKeyboardButton("Назад",callback_data = cd.new('fsm_back_to_catalog'))]
	])

	return Inline

def category_two_pants() -> InlineKeyboardMarkup:
	Inline  = InlineKeyboardMarkup(row_width = 2,inline_keyboard = [	
		[InlineKeyboardButton("Кроссовки",callback_data = cd.new("fsm_Кроссовки"))],
		[InlineKeyboardButton("Туфли",callback_data = cd.new("fsm_Туфли"))],
		[InlineKeyboardButton("Сандали",callback_data = cd.new("fsm_Сандали"))],
		[InlineKeyboardButton("Сапоги",callback_data = cd.new("fsm_Сапоги"))],
		[InlineKeyboardButton("Назад",callback_data = cd.new('fsm_back_to_catalog'))]
	])

	return Inline

def category_two_accessories() -> InlineKeyboardMarkup:
	Inline  = InlineKeyboardMarkup(row_width = 2,inline_keyboard = [	
		[InlineKeyboardButton("Кроссовки",callback_data = cd.new("fsm_Кроссовки"))],
		[InlineKeyboardButton("Туфли",callback_data = cd.new("fsm_Туфли"))],
		[InlineKeyboardButton("Сандали",callback_data = cd.new("fsm_Сандали"))],
		[InlineKeyboardButton("Сапоги",callback_data = cd.new("fsm_Сапоги"))],
		[InlineKeyboardButton("Назад",callback_data = cd.new('fsm_back_to_catalog'))]
	])

	return Inline
