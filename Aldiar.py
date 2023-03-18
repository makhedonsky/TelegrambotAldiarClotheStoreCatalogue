from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher 
from aiogram.utils import executor 
from aiogram.utils.callback_data import CallbackData
from keyboard import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

import os 

TOKEN="5600509943:AAGPSdTH5HdffKE0u_YHXLEBPnsMlphnHvI"


class FSM_admin(StatesGroup):

	photo = State()
	gender = State()
	category1 = State()
	category2 = State()
	name = State()
	price = State()

storage = MemoryStorage()
bot = Bot(TOKEN)
dp = Dispatcher(bot,storage = storage)

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
	await callback.message.edit_text(HELP,reply_markup=help_keyboard())

@dp.callback_query_handler(cd.filter(action = "Каталог"))
async def callback_Catalog(callback:types.CallbackQuery):
	await callback.message.edit_text('Выберите категорию : ',reply_markup = catalog_menu())

@dp.callback_query_handler(cd.filter(action = "partner"))
async def partner_cmd(callback:types.CallbackQuery):
	await callback.message.edit_text("За каждого приглашенного участника вы получаете 200 руб бонуса,которые вы впоследствии \
							можете использовать для получения скидки на заказ. Для этого оправте ему копию партнерской \
							ссылки из раздела \" Получить портнерскую ссылку \"Максимальная скидка но одну товарную позицию 1000р. \
							При стоимость товорной позиции более 20 000р максиальная скидка 2000р ", reply_markup = partner_menu())

@dp.callback_query_handler(cd.filter(action = 'new_goods'))
async def new_goods_cmd(callback:types.Message,state:FSMContext):
	await callback.message.answer('отправьте фото товара ')
	await FSM_admin.photo.set()

@dp.message_handler(lambda message: not message.photo,state = FSM_admin.photo)
async def check_photo(message:types.Message):
	await message.answer("это не фото")

@dp.message_handler(lambda message: message.photo,content_types = ['photo'],state = FSM_admin.photo)
async def photo_fsm(message:types.Message,state:FSMContext):
	async with state.proxy() as data:
		data["photo"] = message.photo[0].file_id	

	await message.answer("теперь выбери категорию",reply_markup = men_women())
	await FSM_admin.next()

@dp.callback_query_handler(cd.filter(action = "Женская"),state = FSM_admin.gender)
async def gender_menu_cmd(callback:types.CallbackQuery,state:FSMContext):
	async with state.proxy() as data:
		data["gender"] = callback.data
	print(callback.data)

	await callback.message.answer("теперь выбери какой тип одежды",reply_markup =category_one())
	await FSM_admin.next()

@dp.callback_query_handler(cd.filter(action = "Мужская"),state = FSM_admin.gender)
async def gender_menu_cmd(callback:types.CallbackQuery,state:FSMContext):
	async with state.proxy() as data:
		data["gender"] = callback.data
	print(callback.data)

	await callback.message.answer("теперь выбери какой тип одежды",reply_markup =category_one())
	await FSM_admin.next()

@dp.callback_query_handler(cd.filter(action = "FSM_shoes"),state = FSM_admin.category1)
async def category1(callback:types.CallbackQuery,state:FSMContext):
	async with state.proxy() as data:
		data["category1"] = callback.data
	print(callback.data)
	await callback.message.answer("какую обувь вы хотите",reply_markup = category_two_shoes())
	await FSM_admin.next()

@dp.callback_query_handler(cd.filter(action = "FSM_Outerwear"),state = FSM_admin.category1)
async def category1(callback:types.CallbackQuery,state:FSMContext):
	async with state.proxy() as data:
		data["category1"] = callback.data
	print(callback.data)
	await callback.message.answer("какую обувь вы хотите",reply_markup = category_two_outerwear())
	await FSM_admin.next()   

@dp.callback_query_handler(cd.filter(action = "FSM_Pants"),state = FSM_admin.category1)
async def category1(callback:types.CallbackQuery,state:FSMContext):
	async with state.proxy() as data:
		data["category1"] = callback.data
	print(callback.data)
	await callback.message.answer("какую обувь вы хотите",reply_markup = category_two_pants())
	await FSM_admin.next()

@dp.callback_query_handler(cd.filter(action = "FSM_Accessories"),state = FSM_admin.category1)
async def category1(callback:types.CallbackQuery,state:FSMContext):
	async with state.proxy() as data:
		data["category1"] = callback.data
	print(callback.data)
	await callback.message.answer("какую обувь вы хотите",reply_markup = category_two_accessories())
	await FSM_admin.next()

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

# ********************************************************************** women Обувь **************************************************************************************


@dp.callback_query_handler(cd.filter(action = "women_Кроссовки"))
async def Sneakers_cmd(message:types.Message):
	await bot.send_photo(message.from_user.id,"https://sunmag.me/wp-content/uploads/2020/09/sunmag-1-65.jpg",caption = "удобная",reply_markup = things())

@dp.callback_query_handler(cd.filter(action = "women_Туфли"))
async def Sneakers_cmd(message:types.Message):
	await bot.send_photo(message.from_user.id,"https://sunmag.me/wp-content/uploads/2020/09/sunmag-1-65.jpg",caption = "удобная",reply_markup = things())

@dp.callback_query_handler(cd.filter(action = "women_Сандали"))
async def Sneakers_cmd(message:types.Message):
	await bot.send_photo(message.from_user.id,"https://sunmag.me/wp-content/uploads/2020/09/sunmag-1-65.jpg",caption = "удобная",reply_markup = things())

@dp.callback_query_handler(cd.filter(action = "women_Сапоги"))
async def Sneakers_cmd(message:types.Message):
	await bot.send_photo(message.from_user.id,"https://sunmag.me/wp-content/uploads/2020/09/sunmag-1-65.jpg",caption = "удобная",reply_markup = things())

@dp.callback_query_handler(cd.filter(action = "back_to_photo"))
async def back_to_photo_cmd(callback:types.CallbackQuery):
	await callback.message.answer("Выберите категорию :",reply_markup = women_shoes_menu())

# ********************************************************************** men Обувь **************************************************************************************

@dp.callback_query_handler(cd.filter(action = "men_Кроссовки"))
async def Sneakers_cmd(message:types.Message):
	await bot.send_photo(message.from_user.id,"https://sunmag.me/wp-content/uploads/2020/09/sunmag-1-65.jpg",caption = "удобная",reply_markup = things())

@dp.callback_query_handler(cd.filter(action = "men_Туфли"))
async def Sneakers_cmd(message:types.Message):
	await bot.send_photo(message.from_user.id,"https://sunmag.me/wp-content/uploads/2020/09/sunmag-1-65.jpg",caption = "удобная",reply_markup = things())

@dp.callback_query_handler(cd.filter(action = "men_Сандали"))
async def Sneakers_cmd(message:types.Message):
	await bot.send_photo(message.from_user.id,"https://sunmag.me/wp-content/uploads/2020/09/sunmag-1-65.jpg",caption = "удобная",reply_markup = things())

@dp.callback_query_handler(cd.filter(action = "men_Сапоги"))
async def Sneakers_cmd(message:types.Message):
	await bot.send_photo(message.from_user.id,"https://sunmag.me/wp-content/uploads/2020/09/sunmag-1-65.jpg",caption = "удобная",reply_markup = things())

@dp.callback_query_handler(cd.filter(action = "back_to_photo"))
async def back_to_photo_cmd(callback:types.CallbackQuery):
	await callback.message.answer("Выберите категорию :",reply_markup = men_shoes_menu())

# ********************************************************************** women Верхняя одежда **************************************************************************************

@dp.callback_query_handler(cd.filter(action = "women_Курткий"))
async def Sneakers_cmd(message:types.Message):
	await bot.send_photo(message.from_user.id,"https://sunmag.me/wp-content/uploads/2020/09/sunmag-1-65.jpg",caption = "удобная",reply_markup = things2())

@dp.callback_query_handler(cd.filter(action = "women_Кофты"))
async def Sneakers_cmd(message:types.Message):
	await bot.send_photo(message.from_user.id,"https://sunmag.me/wp-content/uploads/2020/09/sunmag-1-65.jpg",caption = "удобная",reply_markup = things2())

@dp.callback_query_handler(cd.filter(action = "women_Свиторы"))
async def Sneakers_cmd(message:types.Message):
	await bot.send_photo(message.from_user.id,"https://sunmag.me/wp-content/uploads/2020/09/sunmag-1-65.jpg",caption = "удобная",reply_markup = things2())

@dp.callback_query_handler(cd.filter(action = "women_Дождевик"))
async def Sneakers_cmd(message:types.Message):
	await bot.send_photo(message.from_user.id,"https://sunmag.me/wp-content/uploads/2020/09/sunmag-1-65.jpg",caption = "удобная",reply_markup = things2())

@dp.callback_query_handler(cd.filter(action = "back_to_photo2"))
async def back_to_photo_cmd(callback:types.CallbackQuery):
	await callback.message.answer("Выберите категорию :",reply_markup = women_Outerwear())

# ********************************************************************** men Верхняя одежда **************************************************************************************

@dp.callback_query_handler(cd.filter(action = "men_Курткий"))
async def Sneakers_cmd(message:types.Message):
	await bot.send_photo(message.from_user.id,"https://sunmag.me/wp-content/uploads/2020/09/sunmag-1-65.jpg",caption = "удобная",reply_markup = things())

@dp.callback_query_handler(cd.filter(action = "men_Кофты"))
async def Sneakers_cmd(message:types.Message):
	await bot.send_photo(message.from_user.id,"https://sunmag.me/wp-content/uploads/2020/09/sunmag-1-65.jpg",caption = "удобная",reply_markup = things())

@dp.callback_query_handler(cd.filter(action = "men_Свиторы"))
async def Sneakers_cmd(message:types.Message):
	await bot.send_photo(message.from_user.id,"https://sunmag.me/wp-content/uploads/2020/09/sunmag-1-65.jpg",caption = "удобная",reply_markup = things())

@dp.callback_query_handler(cd.filter(action = "men_Дождевик"))
async def Sneakers_cmd(message:types.Message):
	await bot.send_photo(message.from_user.id,"https://sunmag.me/wp-content/uploads/2020/09/sunmag-1-65.jpg",caption = "удобная",reply_markup = things())

@dp.callback_query_handler(cd.filter(action = "back_to_photo2"))
async def back_to_photo_cmd(callback:types.CallbackQuery):
	await callback.message.answer("Выберите категорию :",reply_markup = men_Outerwear())

# ********************************************************************** men Верхняя одежда ************************************************************************************


@dp.callback_query_handler(cd.filter(action = "back_to_photo"))
async def back_to_photo_cmd(callback:types.CallbackQuery):
	await callback.message.answer("Выберите категорию :",reply_markup = men_shoes_menu())

@dp.callback_query_handler(cd.filter(action = "back_to_photo"))
async def back_to_photo_cmd(callback:types.CallbackQuery):
	await callback.message.answer("Выберите категорию :",reply_markup = women_shoes_menu())



if __name__ == "__main__":
	executor.start_polling(dp,on_startup = on_startup)

