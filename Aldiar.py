from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher 
from aiogram.utils import executor 
from aiogram.utils.callback_data import CallbackData
from keyboard import cd, getInline, getInline2, getInline3

import os 

bot = Bot(os.getenv("TOKEN"))
dp = Dispatcher(bot)

HELP = """
	Каталог - для просмотра нашего товара,
	Для заказа - если хотите закзать наш товар,
	Помощь - для ознокомление с функцианалом бота,
	Партнерам - если есть предложение для сотрудничество,
	Опубликовать товар - что то будет делать
"""

async def on_startup(_):
	print("бот вошел в онлайн")

@dp.message_handler(commands = ["start"])
async def start_cmd(message:types.Message):
	await message.answer("Добро пожаловать в главное меню магазина!\
						Мы продаем только в люсовом качаесте \
						По вопросам по использованию бота можете написать на номер 8-777-77-77",reply_markup = getInline())

@dp.callback_query_handler(cd.filter(action = "help"))
async def callback_help(callback:types.CallbackQuery):
	await callback.message.edit_text(HELP,reply_markup=getInline())

@dp.callback_query_handler(cd.filter(action = "Каталог"))
async def callback_Catalog(callback:types.CallbackQuery):
	await callback.message.edit_text('Выберите категорию : ',reply_markup = getInline4())

@dp.callback_query_handler(cd.filter(action = "partner"))
async def partner_cmd(callback:types.CallbackQuery):
	await callback.message.edit_text("За каждого приглашенного участника вы получаете 200 руб бонуса,которые вы впоследствии \
								можете использовать для получения скидки на заказ. Для этого оправте ему копию партнерской \
								ссылки из раздела \" Получить портнерскую ссылку \" Максимальная скидка но одну товарную позицию 1000р. \
								При стоимость товорной позиции более 20 000р максиальная скидка 2000р ", reply_markup = getInline2())

@dp.callback_query_handler(cd.filter(action = "count"))
async def count_cmd(callback:types.CallbackQuery):
	await callback.message.edit_text("Мои баллы: \
									\n Вы пригласили : 6 человек.\
									Начислено баллов 1200,00",reply_markup = getInline2())

@dp.callback_query_handler(cd.filter(action = "Поделиться"))
async def share_cmd(callback:types.CallbackQuery):
	await callback.message.edit_text('Расскажи друзьям в соц сетях: ',reply_markup = getInline3())

@dp.callback_query_handler(cd.filter(action = "women"))
async def share_cmd(callback:types.CallbackQuery):
	await callback.message.edit_text('')

if __name__ == "__main__":
	executor.start_polling(dp,on_startup = on_startup)
