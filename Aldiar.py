from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher 
from aiogram.utils import executor 
from aiogram.utils.callback_data import CallbackData
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from keyboard import *
from aldiarSQL import *
import os 

TOKEN="5600509943:AAGPSdTH5HdffKE0u_YHXLEBPnsMlphnHvI"

storage = MemoryStorage()
bot = Bot(token=TOKEN)
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

class delete_fsm(StatesGroup):
	name = State()
	Category = State()
	price = State()



@dp.message_handler(commands = ["start"])
async def start_cmd(message:types.Message):
	global res
	await message.answer("Добро пожаловать в главное меню магазина!\n\
		Мы продаем только в люксовом качестве \n\
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

@dp.callback_query_handler( cd.filter(action = "back_to_main"))
@dp.callback_query_handler( cd.filter(action = "back_to_main"),state="*")
async def back_cmd(callback:types.CallbackQuery, state: FSMContext):
	global CURRENT_LEVEL
	CURRENT_LEVEL = 0
	await state.finish()
	await callback.message.edit_text("Вы вернулись в главное меню магазина!\n\
		Мы продаем только в люксовом качестве \n\
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
	global choise1category
	choise1category = 'Обувь'
	await callback.message.edit_text('Выберите категорию : ',reply_markup = women_shoes_menu() )

@dp.callback_query_handler(cd.filter(action = "men_shoes"))
async def men_shoes_menu_cmd(callback:types.CallbackQuery):
	global choise1category
	choise1category = 'Обувь'
	await callback.message.edit_text('Выберите категорию : ',reply_markup = men_shoes_menu() )

@dp.callback_query_handler(cd.filter(action = "WomenOuterwear"))
async def women_Outerwear_cmd(callback:types.CallbackQuery):
	global choise1category
	choise1category = 'Верхняя одежда'
	await callback.message.edit_text('Выберите категорию : ',reply_markup = women_Outerwear() )

@dp.callback_query_handler(cd.filter(action = "MenOuterwear"))
async def men_Outerwear_cmd(callback:types.CallbackQuery):
	global choise1category
	choise1category = 'Верхняя одежда'
	await callback.message.edit_text('Выберите категорию : ',reply_markup = men_Outerwear() )

@dp.callback_query_handler(cd.filter(action = "WomenPants"))
async def women_pants_cmd(callback:types.CallbackQuery):
	global choise1category
	choise1category = 'Штаны'
	await callback.message.edit_text('Выберите категорию : ',reply_markup = women_pants() )	

@dp.callback_query_handler(cd.filter(action = "MenPants"))
async def men_pants_cmd(callback:types.CallbackQuery):
	global choise1category
	choise1category = 'Штаны'
	await callback.message.edit_text('Выберите категорию : ',reply_markup = men_pants() )

@dp.callback_query_handler(cd.filter(action = "WomenAccessories"))
async def women_accessories_cmd(callback:types.CallbackQuery):
	global choise1category
	choise1category = 'Аксессуары'
	await callback.message.edit_text('Выберите категорию : ',reply_markup = women_accessories() )	

@dp.callback_query_handler(cd.filter(action = "MenAccessories"))
async def men_accessories_cmd(callback:types.CallbackQuery):
	global choise1category
	choise1category = 'Аксессуары'
	await callback.message.edit_text('Выберите категорию : ',reply_markup = men_accessories() )

# ********************************************************************** women Обувь **************************************************************************************


@dp.callback_query_handler(cd.filter(action = "women_Кроссовки"))
async def women_sneakers(callback:types.CallbackQuery):	
	global res
	res = sql_female_select(choise1category,"Кроссовки")
	await callback.message.delete()
	await bot.send_photo(callback.message.chat.id, res[CURRENT_LEVEL][1], caption = f'{res[CURRENT_LEVEL][2]} \n{res[CURRENT_LEVEL][3]}',reply_markup = things(len(res),CURRENT_LEVEL))

@dp.callback_query_handler(cd.filter(action = "women_Туфли"))
async def women_heels(callback:types.CallbackQuery):
	global res
	res = sql_female_select(choise1category,"Туфли")
	await callback.message.delete()
	await bot.send_photo(callback.message.chat.id, res[CURRENT_LEVEL][1], caption = f'{res[CURRENT_LEVEL][2]} \n{res[CURRENT_LEVEL][3]}',reply_markup = things(len(res),CURRENT_LEVEL))

@dp.callback_query_handler(cd.filter(action = "women_Сандали"))
async def women_sandals(callback:types.CallbackQuery):
	global res
	res = sql_female_select(choise1category,"Сандали")
	await callback.message.delete()
	await bot.send_photo(callback.message.chat.id, res[CURRENT_LEVEL][1], caption = f'{res[CURRENT_LEVEL][2]} \n{res[CURRENT_LEVEL][3]}',reply_markup = things(len(res),CURRENT_LEVEL))

@dp.callback_query_handler(cd.filter(action = "women_Сапоги"))
async def women_boots(callback:types.CallbackQuery):
	global res
	res = sql_female_select(choise1category,"Сапоги")
	await callback.message.delete()
	await bot.send_photo(callback.message.chat.id, res[CURRENT_LEVEL][1], caption = f'{res[CURRENT_LEVEL][2]} \n{res[CURRENT_LEVEL][3]}',reply_markup = things(len(res),CURRENT_LEVEL))

# ********************************************************************** men Обувь **************************************************************************************

@dp.callback_query_handler(cd.filter(action = "men_Кроссовки"))
async def men_sneakers(callback:types.CallbackQuery):
	global res
	res = sql_male_select(choise1category,"Кроссовки")
	await callback.message.delete()
	await bot.send_photo(callback.message.chat.id, res[CURRENT_LEVEL][1], caption = f'{res[CURRENT_LEVEL][2]} \n{res[CURRENT_LEVEL][3]}',reply_markup = things(len(res),CURRENT_LEVEL))

@dp.callback_query_handler(cd.filter(action = "men_Туфли"))
async def men_heels(callback:types.CallbackQuery):
	global res
	res = sql_male_select(choise1category,"Туфли")
	await callback.message.delete()
	await bot.send_photo(callback.message.chat.id, res[CURRENT_LEVEL][1], caption = f'{res[CURRENT_LEVEL][2]} \n{res[CURRENT_LEVEL][3]}',reply_markup = things(len(res),CURRENT_LEVEL))

@dp.callback_query_handler(cd.filter(action = "men_Сандали"))
async def men_sandals(callback:types.CallbackQuery):
	global res
	res = sql_male_select(choise1category,"Сандали")
	await callback.message.delete()
	await bot.send_photo(callback.message.chat.id, res[CURRENT_LEVEL][1], caption = f'{res[CURRENT_LEVEL][2]} \n{res[CURRENT_LEVEL][3]}',reply_markup = things(len(res),CURRENT_LEVEL))

@dp.callback_query_handler(cd.filter(action = "men_Сапоги"))
async def man_boots(callback:types.CallbackQuery):
	global res
	res = sql_male_select(choise1category,"Сапоги")
	await callback.message.delete()
	await bot.send_photo(callback.message.chat.id, res[CURRENT_LEVEL][1], caption = f'{res[CURRENT_LEVEL][2]} \n{res[CURRENT_LEVEL][3]}',reply_markup = things(len(res),CURRENT_LEVEL))


# ********************************************************************** women Верхняя одежда **************************************************************************************

@dp.callback_query_handler(cd.filter(action = "women_Куртки"))
async def women_jackets(callback:types.CallbackQuery):
	global res
	res = sql_female_select(choise1category,"Куртки")
	await callback.message.delete()
	await bot.send_photo(callback.message.chat.id, res[CURRENT_LEVEL][1], caption = f'{res[CURRENT_LEVEL][2]} \n{res[CURRENT_LEVEL][3]}',reply_markup = things(len(res),CURRENT_LEVEL))

@dp.callback_query_handler(cd.filter(action = "women_Кофты"))
async def women_blouses(message:types.Message):
	global res
	res = sql_female_select(choise1category,"Кофты")
	await callback.message.delete()
	await bot.send_photo(callback.message.chat.id, res[CURRENT_LEVEL][1], caption = f'{res[CURRENT_LEVEL][2]} \n{res[CURRENT_LEVEL][3]}',reply_markup = things(len(res),CURRENT_LEVEL))

@dp.callback_query_handler(cd.filter(action = "women_Свиторы"))
async def women_sweaters(callback:types.CallbackQuery):
	global res
	res = sql_female_select(choise1category,"Свиторы")
	await callback.message.delete()
	await bot.send_photo(callback.message.chat.id, res[CURRENT_LEVEL][1], caption = f'{res[CURRENT_LEVEL][2]} \n{res[CURRENT_LEVEL][3]}',reply_markup = things(len(res),CURRENT_LEVEL))

@dp.callback_query_handler(cd.filter(action = "women_Дождевик"))
async def women_raincoats(callback:types.CallbackQuery):
	global res
	res = sql_female_select(choise1category,"Дождевик")
	await callback.message.delete()
	await bot.send_photo(callback.message.chat.id, res[CURRENT_LEVEL][1], caption = f'{res[CURRENT_LEVEL][2]} \n{res[CURRENT_LEVEL][3]}',reply_markup = things(len(res),CURRENT_LEVEL))


# ********************************************************************** men Верхняя одежда **************************************************************************************

@dp.callback_query_handler(cd.filter(action = "men_Куртки"))
async def men_jackets(callback:types.CallbackQuery):
	global res
	res = sql_male_select(choise1category,"Куртки")
	await callback.message.delete()
	await bot.send_photo(callback.message.chat.id, res[CURRENT_LEVEL][1], caption = f'{res[CURRENT_LEVEL][2]} \n{res[CURRENT_LEVEL][3]}',reply_markup = things(len(res),CURRENT_LEVEL))


@dp.callback_query_handler(cd.filter(action = "men_Кофты"))#    THE ONLY WORKING HANDLER
async def men_blouses(callback:types.CallbackQuery):
  global res
  res = sql_male_select(choise1category,"Кофты")
  await callback.message.delete()
  await bot.send_photo(callback.message.chat.id, res[CURRENT_LEVEL][1], caption = f'{res[CURRENT_LEVEL][2]} \n{res[CURRENT_LEVEL][3]}',reply_markup = things(len(res),CURRENT_LEVEL))

@dp.callback_query_handler(cd.filter(action = "men_Свиторы"))
async def men_sweaters(callback:types.CallbackQuery):
	global res
	res = sql_male_select(choise1category,"Свиторы")
	await callback.message.delete()
	await bot.send_photo(callback.message.chat.id, res[CURRENT_LEVEL][1], caption = f'{res[CURRENT_LEVEL][2]} \n{res[CURRENT_LEVEL][3]}',reply_markup = things(len(res),CURRENT_LEVEL))

@dp.callback_query_handler(cd.filter(action = "men_Дождевик"))
async def men_raincoats(callback:types.CallbackQuery):
	global res
	res = sql_male_select(choise1category,"Дождевик")
	await callback.message.delete()
	await bot.send_photo(callback.message.chat.id, res[CURRENT_LEVEL][1], caption = f'{res[CURRENT_LEVEL][2]} \n{res[CURRENT_LEVEL][3]}',reply_markup = things(len(res),CURRENT_LEVEL))



# ********************************************************************** men PANTS ************************************************************************************


@dp.callback_query_handler(cd.filter(action = "men_Трико"))
async def men_tights(callback:types.CallbackQuery):
	global res
	res = sql_male_select(choise1category,"Трико")
	await callback.message.delete()
	await bot.send_photo(callback.message.chat.id, res[CURRENT_LEVEL][1], caption = f'{res[CURRENT_LEVEL][2]} \n{res[CURRENT_LEVEL][3]}',reply_markup = things(len(res),CURRENT_LEVEL))

@dp.callback_query_handler(cd.filter(action = "men_Джинсы"))
async def men_jeans(callback:types.CallbackQuery):
	global res
	res = sql_male_select(choise1category,"Джинсы")
	await callback.message.delete()
	await bot.send_photo(callback.message.chat.id, res[CURRENT_LEVEL][1], caption = f'{res[CURRENT_LEVEL][2]} \n{res[CURRENT_LEVEL][3]}',reply_markup = things(len(res),CURRENT_LEVEL))

@dp.callback_query_handler(cd.filter(action = "men_Лосины"))
async def men_leggings(callback:types.CallbackQuery):
	global res
	res = sql_male_select(choise1category,"Лосины")
	await callback.message.delete()
	await bot.send_photo(callback.message.chat.id, res[CURRENT_LEVEL][1], caption = f'{res[CURRENT_LEVEL][2]} \n{res[CURRENT_LEVEL][3]}',reply_markup = things(len(res),CURRENT_LEVEL))

@dp.callback_query_handler(cd.filter(action = "men_Классические брюки"))
async def men_classic_pants(callback:types.CallbackQuery):
	global res
	res = sql_male_select(choise1category,"Классические брюки")
	await callback.message.delete()
	await bot.send_photo(callback.message.chat.id, res[CURRENT_LEVEL][1], caption = f'{res[CURRENT_LEVEL][2]} \n{res[CURRENT_LEVEL][3]}',reply_markup = things(len(res),CURRENT_LEVEL))




# ********************************************************************** women PANTS ************************************************************************************


@dp.callback_query_handler(cd.filter(action = "women_Трико"))
async def women_tights(callback:types.CallbackQuery):
	global res
	res = sql_female_select(choise1category,"Трико")
	await callback.message.delete()
	await bot.send_photo(callback.message.chat.id, res[CURRENT_LEVEL][1], caption = f'{res[CURRENT_LEVEL][2]} \n{res[CURRENT_LEVEL][3]}',reply_markup = things(len(res),CURRENT_LEVEL))

@dp.callback_query_handler(cd.filter(action = "women_Джинсы"))
async def women_jeans(callback:types.CallbackQuery):
	global res
	res = sql_female_select(choise1category,"Джинсы")
	await callback.message.delete()
	await bot.send_photo(callback.message.chat.id, res[CURRENT_LEVEL][1], caption = f'{res[CURRENT_LEVEL][2]} \n{res[CURRENT_LEVEL][3]}',reply_markup = things(len(res),CURRENT_LEVEL))

@dp.callback_query_handler(cd.filter(action = "women_Лосины"))
async def women_leggings(callback:types.CallbackQuery):
	global res
	res = sql_female_select(choise1category,"Лосины")
	await callback.message.delete()
	await bot.send_photo(callback.message.chat.id, res[CURRENT_LEVEL][1], caption = f'{res[CURRENT_LEVEL][2]} \n{res[CURRENT_LEVEL][3]}',reply_markup = things(len(res),CURRENT_LEVEL))

@dp.callback_query_handler(cd.filter(action = "women_Классические брюки"))
async def women_classic_pants(callback:types.CallbackQuery):
	global res
	res = sql_female_select(choise1category,"Классические брюки")
	await callback.message.delete()
	await bot.send_photo(callback.message.chat.id, res[CURRENT_LEVEL][1], caption = f'{res[CURRENT_LEVEL][2]} \n{res[CURRENT_LEVEL][3]}',reply_markup = things(len(res),CURRENT_LEVEL))




# ********************************************************************** men ACCESSORIES ************************************************************************************


@dp.callback_query_handler(cd.filter(action = "men_Очки"))
async def men_glasses(callback:types.CallbackQuery):
	global res
	res = sql_male_select(choise1category,"Очки")
	await callback.message.delete()
	await bot.send_photo(callback.message.chat.id, res[CURRENT_LEVEL][1], caption = f'{res[CURRENT_LEVEL][2]} \n{res[CURRENT_LEVEL][3]}',reply_markup = things(len(res),CURRENT_LEVEL))

@dp.callback_query_handler(cd.filter(action = "men_Часы"))
async def men_watches(callback:types.CallbackQuery):
	global res
	res = sql_male_select(choise1category,"Часы")
	await callback.message.delete()
	await bot.send_photo(callback.message.chat.id, res[CURRENT_LEVEL][1], caption = f'{res[CURRENT_LEVEL][2]} \n{res[CURRENT_LEVEL][3]}',reply_markup = things(len(res),CURRENT_LEVEL))

@dp.callback_query_handler(cd.filter(action = "men_Сумки"))
async def men_bags(callback:types.CallbackQuery):
	global res
	res = sql_male_select(choise1category,"Сумки")
	await callback.message.delete()
	await bot.send_photo(callback.message.chat.id, res[CURRENT_LEVEL][1], caption = f'{res[CURRENT_LEVEL][2]} \n{res[CURRENT_LEVEL][3]}',reply_markup = things(len(res),CURRENT_LEVEL))

@dp.callback_query_handler(cd.filter(action = "men_Кольцо"))
async def men_ring(callback:types.CallbackQuery):
	global res
	res = sql_male_select(choise1category,"Кольцо")
	await callback.message.delete()
	await bot.send_photo(callback.message.chat.id, res[CURRENT_LEVEL][1], caption = f'{res[CURRENT_LEVEL][2]} \n{res[CURRENT_LEVEL][3]}',reply_markup = things(len(res),CURRENT_LEVEL))



# ********************************************************************** women ACCESSORIES ************************************************************************************


@dp.callback_query_handler(cd.filter(action = "women_Очки"))
async def women_glasses(callback:types.CallbackQuery):
	global res
	res = sql_female_select(choise1category,"Очки")
	await callback.message.delete()
	await bot.send_photo(callback.message.chat.id, res[CURRENT_LEVEL][1], caption = f'{res[CURRENT_LEVEL][2]} \n{res[CURRENT_LEVEL][3]}',reply_markup = things(len(res),CURRENT_LEVEL))

@dp.callback_query_handler(cd.filter(action = "women_Часы"))
async def women_watches(callback:types.CallbackQuery):
	global res
	res = sql_female_select(choise1category,"Часы")
	await callback.message.delete()
	await bot.send_photo(callback.message.chat.id, res[CURRENT_LEVEL][1], caption = f'{res[CURRENT_LEVEL][2]} \n{res[CURRENT_LEVEL][3]}',reply_markup = things(len(res),CURRENT_LEVEL))

@dp.callback_query_handler(cd.filter(action = "women_Сумки"))
async def women_bags(callback:types.CallbackQuery):
	global res
	res = sql_female_select(choise1category,"Сумки")
	await callback.message.delete()
	await bot.send_photo(callback.message.chat.id, res[CURRENT_LEVEL][1], caption = f'{res[CURRENT_LEVEL][2]} \n{res[CURRENT_LEVEL][3]}',reply_markup = things(len(res),CURRENT_LEVEL))

@dp.callback_query_handler(cd.filter(action = "women_Кольцо"))
async def women_ring(callback:types.CallbackQuery):
	global res
	res = sql_female_select(choise1category,"Кольцо")
	await callback.message.delete()
	await bot.send_photo(callback.message.chat.id, res[CURRENT_LEVEL][1], caption = f'{res[CURRENT_LEVEL][2]} \n{res[CURRENT_LEVEL][3]}',reply_markup = things(len(res),CURRENT_LEVEL))




















CURRENT_LEVEL = 0


@dp.callback_query_handler(cd.filter(action = "Следующий"))
async def next_product(callback:types.CallbackQuery):
	global CURRENT_LEVEL
	CURRENT_LEVEL = CURRENT_LEVEL + 1
	print(len(res), '	res')
	print(CURRENT_LEVEL, '	CURRENT_LEVEL')
	await callback.message.edit_media(types.InputMedia(media = res[CURRENT_LEVEL][1], type = 'photo', caption = f'{res[CURRENT_LEVEL][2]} \n{res[CURRENT_LEVEL][3]}'),reply_markup = things(len(res),CURRENT_LEVEL))

@dp.callback_query_handler(cd.filter(action = "Предыдущий"))
async def previous_product(callback:types.CallbackQuery):
	global CURRENT_LEVEL
	CURRENT_LEVEL = CURRENT_LEVEL - 1
	await callback.message.edit_media(types.InputMedia(media = res[CURRENT_LEVEL][1], type = 'photo', caption = f'{res[CURRENT_LEVEL][2]} \n{res[CURRENT_LEVEL][3]}'),reply_markup = things(len(res),CURRENT_LEVEL))

@dp.callback_query_handler(cd.filter(action = "back_from_things"))
async def callback_Catalog(callback:types.CallbackQuery):
	await callback.message.delete()
	await callback.message.answer('Выберите категорию : ',reply_markup = catalog_menu())











#####################################################################		ADD PRODUCTS	#################################


@dp.callback_query_handler(cd.filter(action = 'new_product'))
async def new_product_cmd(callback:types.Message):
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
		data["category2"] = callback.data[10:]
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
	await message.answer("Вы вернулись в главное меню магазина!\n\
		Мы продаем только в люксовом качестве \n\
		По вопросам по использованию бота можете написать на номер 8-777-77-77",reply_markup = main_menu())

##########################################################################################################################

@dp.callback_query_handler(cd.filter(action = 'delete_goods'))
async def new_product_cmd(callback:types.CallbackQuery):
	await callback.message.answer("напишите имя товара")
	await delete_fsm.name.set()

@dp.message_handler(state = delete_fsm.name)
async def cmd_get_name(callback:types.Message,state:FSMContext):
	async with state.proxy() as data:
		data["name"] = callback.text
	print(type(callback.text))
	await callback.answer('напишите выберите категорию',reply_markup = Category())
	await delete_fsm.next()

@dp.callback_query_handler(cd.filter( action = "Shoes"),state = delete_fsm.Category)
async def cmd_get(callback:types.CallbackQuery,state:FSMContext):
	async with state.proxy() as data:
		data["Category"] = "Shoes"
	await callback.message.answer('напишите цену товара')
	await delete_fsm.next()


@dp.callback_query_handler(cd.filter(action = "Outerwear"),state = delete_fsm.Category)
async def cmd_get(callback:types.CallbackQuery,state:FSMContext):
	async with state.proxy() as data:
		data["Category"] = "Outerwear"
	await callback.message.answer('напишите цену товара')
	await delete_fsm.next()


@dp.callback_query_handler(cd.filter(action = "Pants"),state = delete_fsm.Category)
async def cmd_get(callback:types.CallbackQuery,state:FSMContext):
	async with state.proxy() as data:
		data["Category"] = "Pants"
	await callback.message.answer('напишите цену товара')
	await delete_fsm.next()


@dp.callback_query_handler(cd.filter(action = "Accessories"),state = delete_fsm.Category)
async def cmd_get(callback:types.CallbackQuery,state:FSMContext):
	async with state.proxy() as data:
		data["Category"] = "Accessories"
	await callback.message.answer('напишите цену товара')
	await delete_fsm.next()


@dp.message_handler(state = delete_fsm.price)
async def cmd_get_price(message:types.Message,state:FSMContext):
	async with state.proxy() as data:
		data["price"] = message.text
	print(message.text)
	it_is = mysql(data)
	try:
		await bot.send_photo(message.from_user.id,it_is[1],caption = f"{data['name']}, \nцена - {data['price']}",reply_markup = get_True())
	except TypeError:	
		await message.answer("не нашли ")

	await delete_fsm.next()

@dp.callback_query_handler(cd.filter(action = "Yes"))
async def cmd_yes(message:types.Message,state:FSMContext):
	async with state.proxy() as data :
		delete_something(data)
	await message.message.answer("успешно удалено",reply_markup = main_menu())

@dp.callback_query_handler(cd.filter(action ="No"))
async def cmd_yes(message:types.Message,state:FSMContext):
	await message.message.answer("к сожалению не нашили",reply_markup = main_menu())

##########################################################################################################################

if __name__ == "__main__":
	executor.start_polling(dp,on_startup = on_startup)
