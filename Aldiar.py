from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher 
from aiogram.utils import executor 
from aiogram.utils.callback_data import CallbackData
from inline import cd, main_menu, partner_menu, share_menu, catalog_menu, women_category_menu, men_category_menu, women_shoes_menu, men_shoes_menu,women_Outerwear,men_Outerwear, men_pants, women_pants, Women_Accessories, Men_Accessories

import os 

bot = Bot(os.getenv("TOKEN"))
dp = Dispatcher(bot)

async def on_startup(_):
	print("бот вошел в онлайн")

HELP = """
	Каталог - для просмотра нашего товара,
	Для заказа - если хотите закзать наш товар,
	Помощь - для ознокомление с функцианалом бота,
	Партнерам - если есть предложение для сотрудничество,
	Опубликовать товар - что то будет делать
"""

@dp.message_handler(commands = ["start"])
async def start_cmd(message:types.Message):
	await message.answer("Добро пожаловать в главное меню магазина!\
						Мы продаем только в люсовом качаесте \
						По вопросам по использованию бота можете написать на номер 8-777-77-77",reply_markup = main_menu())

@dp.callback_query_handler(cd.filter(action = "help"))
async def callback_help(callback:types.CallbackQuery):
	await callback.message.edit_text(HELP,reply_markup=main_menu())

@dp.callback_query_handler(cd.filter(action = "Каталог"))
async def callback_Catalog(callback:types.CallbackQuery):
	await callback.message.edit_text('Выберите категорию : ',reply_markup = catalog_menu())

@dp.callback_query_handler(cd.filter(action = "partner"))
async def partner_cmd(callback:types.CallbackQuery):
	await callback.message.edit_text("За каждого приглашенного участника вы получаете 200 руб бонуса,которые вы впоследствии \
							можете использовать для получения скидки на заказ. Для этого оправте ему копию партнерской \
							ссылки из раздела \" Получить портнерскую ссылку \"Максимальная скидка но одну товарную позицию 1000р. \
							При стоимость товорной позиции более 20 000р максиальная скидка 2000р ", reply_markup = partner_menu())

@dp.callback_query_handler(cd.filter(action = "count"))
async def count_cmd(callback:types.CallbackQuery):
	await callback.message.edit_text("Мои баллы: \
									\n Вы пригласили : 6 человек.\
									Начислено баллов 1200,00",reply_markup = partner_menu())

@dp.callback_query_handler(cd.filter(action = "Поделиться"))
async def share_cmd(callback:types.CallbackQuery):
	await callback.message.edit_text('Расскажи друзьям в соц сетях: ',reply_markup = share_menu())

@dp.callback_query_handler(cd.filter(action = "back_to_main"))
async def back_cmd(callback:types.CallbackQuery):
	await callback.message.edit_text("Добро пожаловать в главное меню магазина!\
						Мы продаем только в люсовом качаесте \
						По вопросам по использованию бота можете написать на номер 8-777-77-77",reply_markup = main_menu())

@dp.callback_query_handler(cd.filter(action = "women"))
async def women_cmd(callback:types.CallbackQuery):
	await callback.message.edit_text('Выберите категорию : ',reply_markup = women_category_menu())

@dp.callback_query_handler(cd.filter(action = "men"))
async def men_cmd(callback:types.CallbackQuery):
	await callback.message.edit_text('Выберите категорию : ',reply_markup = men_category_menu())

@dp.callback_query_handler(cd.filter(action = "back_to_catalog"))
async def men_cmd(callback:types.CallbackQuery):
	await callback.message.edit_text('Выберите категорию : ',reply_markup = catalog_menu())

@dp.callback_query_handler(cd.filter(action = "bakc_to_partner"))
async def men_cmd(callback:types.CallbackQuery):
	await callback.message.edit_text("За каждого приглашенного участника вы получаете 200 руб бонуса,которые вы впоследствии \
							можете использовать для получения скидки на заказ. Для этого оправте ему копию партнерской \
							ссылки из раздела \" Получить портнерскую ссылку \"Максимальная скидка но одну товарную позицию 1000р. \
							При стоимость товорной позиции более 20 000р максиальная скидка 2000р ", reply_markup = partner_menu())

@dp.callback_query_handler(cd.filter(action = "women_shoes"))
async def women_shoes_menu_cmd(callback:types.CallbackQuery):
	await callback.message.edit_text('Выберите категорию : ',reply_markup = women_shoes_menu() )

@dp.callback_query_handler(cd.filter(action = "men_shoes"))
async def men_shoes_menu_cmd(callback:types.CallbackQuery):
	await callback.message.edit_text('Выберите категорию : ',reply_markup = men_shoes_menu() )

@dp.callback_query_handler(cd.filter(action = "WomenOuterwear"))
async def women_Outerwear_cmd(callback:types.CallbackQuery):
	await callback.message.edit_text('Выберите категорию : ',reply_markup = women_Outerwear() )

@dp.callback_query_handler(cd.filter(action = "MenOuterwear"))
async def men_Outerwear_cmd(callback:types.CallbackQuery):
	await callback.message.edit_text('Выберите категорию : ',reply_markup = men_Outerwear() )

@dp.callback_query_handler(cd.filter(action = "WomenPants"))
async def women_pants_cmd(callback:types.CallbackQuery):
	await callback.message.edit_text('Выберите категорию : ',reply_markup = women_pants() )	

@dp.callback_query_handler(cd.filter(action = "MenPants"))
async def men_pants_cmd(callback:types.CallbackQuery):
	await callback.message.edit_text('Выберите категорию : ',reply_markup = men_pants() )

@dp.callback_query_handler(cd.filter(action = "WomenAccessories"))
async def Women_Accessories_cmd(callback:types.CallbackQuery):
	await callback.message.edit_text('Выберите категорию : ',reply_markup = Women_Accessories() )	

@dp.callback_query_handler(cd.filter(action = "MenAccessories"))
async def Men_Accessories_cmd(callback:types.CallbackQuery):
	await callback.message.edit_text('Выберите категорию : ',reply_markup = Men_Accessories() )


if __name__ == "__main__":
	executor.start_polling(dp,on_startup = on_startup)

