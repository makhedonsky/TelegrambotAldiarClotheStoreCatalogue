from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher 
from aiogram.utils import executor 
from aiogram.utils.callback_data import CallbackData
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from inline import *
from aldiarSQL import *
import os 

#TOKEN="5600509943:AAGPSdTH5HdffKE0u_YHXLEBPnsMlphnHvI"

storage = MemoryStorage()
bot = Bot(token=os.getenv('TOKEN'))
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

class FSM_admin(StatesGroup):
	photo = State()
	gender = State()
	category1 = State()
	category2 = State()
	name = State()
	price = State()


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



@dp.callback_query_handler(cd.filter(action = "count"))
async def count_cmd(callback:types.CallbackQuery):
	await callback.message.edit_text("Мои баллы: \
									\n Вы пригласили : 6 человек.\
									Начислено баллов 1200,00",reply_markup = partner_menu())

@dp.callback_query_handler(cd.filter(action = "Поделиться"))
async def share_cmd(callback:types.CallbackQuery):
	await callback.message.edit_text('Расскажи друзьям в соц сетях: ',reply_markup = share_menu())

@dp.callback_query_handler( cd.filter(action = "back_to_main"),state="*")
async def back_cmd(callback:types.CallbackQuery, state: FSMContext):
	await state.finish()
	await callback.message.edit_text("Добро пожаловать в главное меню магазина!\n\
						Мы продаем только в люксовом качаесте \n\
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
















#####################################################################		ADD PRODUCTS	#################################


@dp.callback_query_handler(cd.filter(action = 'new_product'))
async def new_product_cmd(callback:types.Message,state:FSMContext):
	await callback.message.answer('Отправьте изображение товара ')
	await FSM_admin.photo.set()

@dp.message_handler(lambda message: not message.photo,state = FSM_admin.photo)
async def add_FSMphoto_check(message:types.Message):
	await message.answer("Ошибка. Отправьте изображение.")

@dp.message_handler(lambda message: message.photo,content_types = ['photo'],state = FSM_admin.photo)
async def add_FSMphoto(message:types.Message,state:FSMContext):
	async with state.proxy() as data:
		data["photo"] = message.photo[0].file_id	
	await message.answer("Выберите одежда для какого пола",reply_markup = men_women())
	await FSM_admin.next()

@dp.callback_query_handler(cd.filter(action = "Женская"),state = FSM_admin.gender)
async def add_FSMcategory_women(callback:types.CallbackQuery,state:FSMContext):
	async with state.proxy() as data:
		data["gender"] = "Женская"
	await callback.message.edit_text("Выберите категорию одежды",reply_markup = add_categoryK())
	await FSM_admin.next()

@dp.callback_query_handler(cd.filter(action = "Мужская"),state = FSM_admin.gender)
async def add_FSMcategory_men(callback:types.CallbackQuery,state:FSMContext):
	async with state.proxy() as data:
		data["gender"] = "Мужская"
	await callback.message.edit_text("Выберите категорию одежды", reply_markup = add_categoryK())
	await FSM_admin.next()



@dp.callback_query_handler(cd.filter(action = "add_shoes"), state = FSM_admin.category1)
async def add_FSMcategory1(callback:types.CallbackQuery,state:FSMContext):
	async with state.proxy() as data:
		data["category1"] = "Обувь"
	await callback.message.edit_text("Выберите тип одежды",reply_markup = add_shoesK())
	await FSM_admin.next()

@dp.callback_query_handler(cd.filter(action = "add_outerwear"), state = FSM_admin.category1)
async def add_FSMcategory1(callback:types.CallbackQuery,state:FSMContext):
	async with state.proxy() as data:
		data["category1"] = "Верхняя одежда"
	await callback.message.edit_text("Выберите тип одежды",reply_markup = add_outerwearK())
	await FSM_admin.next()

@dp.callback_query_handler(cd.filter(action = "add_pants"), state = FSM_admin.category1)
async def add_FSMcategory1(callback:types.CallbackQuery,state:FSMContext):
	async with state.proxy() as data:
		data["category1"] = "Штаны"
	await callback.message.edit_text("Выберите тип одежды",reply_markup = add_pantsK())
	await FSM_admin.next()

@dp.callback_query_handler(cd.filter(action = "add_accessories"), state = FSM_admin.category1)
async def add_FSMcategory1(callback:types.CallbackQuery,state:FSMContext):
	async with state.proxy() as data:
		data["category1"] = "Аксессуары"
	await callback.message.edit_text("Выберите тип одежды",reply_markup = add_accessoriesK())
	await FSM_admin.next()


@dp.callback_query_handler(state = FSM_admin.category2)
async def add_FSMcategory2(callback:types.CallbackQuery,state:FSMContext):
	async with state.proxy() as data:
		data["category2"] = callback.data
	await callback.message.answer("Введите название товара")
	await FSM_admin.next()

@dp.message_handler(lambda message: message.text, content_types = ['text'], state = FSM_admin.name)
async def add_FSMname(message:types.Message,state:FSMContext):
	async with state.proxy() as data:
		data["name"] = message.text
	await message.answer("Введите стоимость товара")
	await FSM_admin.next()

@dp.message_handler(lambda message: message.text, content_types = ['text'], state = FSM_admin.price)
async def add_FSMprice(message:types.Message,state:FSMContext):
	async with state.proxy() as data:
		data["price"] = message.text
	if data['gender'] == "Мужская":
		sql_male(data)
	elif data['gender'] == "Женская":
		sql_female(data)
	await state.finish()


##########################################################################################################################

if __name__ == "__main__":
	executor.start_polling(dp,on_startup = on_startup)
