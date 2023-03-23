import sqlite3
from contextlib import closing




ShoesCreateTable = "CREATE TABLE IF NOT EXISTS Shoes(category2 text, photo text, name text primary key, price text)"
OuterwearCreateTable = "CREATE TABLE IF NOT EXISTS Outerwear(category2 text, photo text, name text primary key, price text)"
PantsCreateTable = "CREATE TABLE IF NOT EXISTS Pants(category2 text, photo text, name text primary key, price text)"
AccessoriesCreateTable = "CREATE TABLE IF NOT EXISTS Accessories(category2 text, photo text, name text primary key, price text)"


connectionM = sqlite3.connect('MaleDB.db')
connectionF = sqlite3.connect('FemaleDB.db')

connectionM.execute(ShoesCreateTable)
connectionM.execute(OuterwearCreateTable)
connectionM.execute(PantsCreateTable)
connectionM.execute(AccessoriesCreateTable)

connectionF.execute(ShoesCreateTable)
connectionF.execute(OuterwearCreateTable)
connectionF.execute(PantsCreateTable)
connectionF.execute(AccessoriesCreateTable)


def sql_male(data):
	connectionM = sqlite3.connect('MaleDB.db')

	if data['category1'] == 'Аксессуары':
		AccessoriesInsertTable = f"INSERT INTO Accessories(category2, photo, name, price) VALUES ('{data['category2']}', '{data['photo']}', '{data['name']}', '{data['price']}')"
		connectionM.execute(AccessoriesInsertTable)

	elif data['category1'] == 'Обувь':
		ShoesInsertTable = f"INSERT INTO Shoes(category2, photo, name, price) VALUES ('{data['category2']}', '{data['photo']}', '{data['name']}', '{data['price']}')"
		connectionM.execute(ShoesInsertTable)

	elif data['category1'] == 'Верхняя одежда':
		OuterwearInsertTable = f"INSERT INTO Outerwear(category2, photo, name, price) VALUES ('{data['category2']}', '{data['photo']}', '{data['name']}', '{data['price']}')"
		connectionM.execute(OuterwearInsertTable)

	elif data['category1'] == 'Штаны':
		PantsInsertTable = f"INSERT INTO Pants(category2, photo, name, price) VALUES ('{data['category2']}', '{data['photo']}', '{data['name']}', '{data['price']}')"
		connectionM.execute(PantsInsertTable)

	connectionM.commit()
	connectionM.close()


def sql_female(data):
	connectionF = sqlite3.connect('FemaleDB.db')

	if data['category1'] == 'Аксессуары':
		AccessoriesInsertTable = f"INSERT INTO Accessories(category2, photo, name, price) VALUES ('{data['category2']}', '{data['photo']}', '{data['name']}', '{data['price']}')"
		connectionF.execute(AccessoriesInsertTable)

	elif data['category1'] == 'Обувь':
		ShoesInsertTable = f"INSERT INTO Shoes(category2, photo, name, price) VALUES ('{data['category2']}', '{data['photo']}', '{data['name']}', '{data['price']}')"
		connectionF.execute(ShoesInsertTable)

	elif data['category1'] == 'Верхняя одежда':
		OuterwearInsertTable = f"INSERT INTO Outerwear(category2, photo, name, price) VALUES ('{data['category2']}', '{data['photo']}', '{data['name']}', '{data['price']}')"
		connectionF.execute(OuterwearInsertTable)

	elif data['category1'] == 'Штаны':
		PantsInsertTable = f"INSERT INTO Pants(category2, photo, name, price) VALUES ('{data['category2']}', '{data['photo']}', '{data['name']}', '{data['price']}')"
		connectionF.execute(PantsInsertTable)

	connectionF.commit()
	connectionF.close()





def sql_male_select(choise, product):
	connectionM = sqlite3.connect('MaleDB.db')
	cursorM = connectionM.cursor()
	global SelectedList

	if choise == 'Аксессуары':
		AccessoriesSelect = f"SELECT * FROM Accessories WHERE category2 = '{product}'"

		cursorM.execute(AccessoriesSelect)
		SelectedList = cursorM.fetchall()


	elif choise == 'Обувь':
		ShoesSelect = f"SELECT * FROM Shoes WHERE category2 = '{product}'"

		cursorM.execute(ShoesSelect)
		SelectedList = cursorM.fetchall()


	elif choise == 'Верхняя одежда':
		OuterwearSelect = f"SELECT * FROM Outerwear WHERE category2 = '{product}'"

		cursorM.execute(OuterwearSelect)
		SelectedList = cursorM.fetchall()


	elif choise == 'Штаны':
		PantsSelect = f"SELECT * FROM Pants WHERE category2 = '{product}'"

		cursorM.execute(PantsSelect)
		SelectedList = cursorM.fetchall()

	return SelectedList



def sql_female_select(choise, product):
	connectionF = sqlite3.connect('FemaleDB.db')
	cursorF = connectionF.cursor()
	global SelectedList

	if choise == 'Аксессуары':
		AccessoriesSelect = f"SELECT * FROM Accessories WHERE category2 = '{product}'"

		cursorF.execute(AccessoriesSelect)
		SelectedList = cursorM.fetchall()


	elif choise == 'Обувь':
		ShoesSelect = f"SELECT * FROM Shoes WHERE category2 = '{product}'"

		cursorF.execute(ShoesSelect)
		SelectedList = cursorF.fetchall()


	elif choise == 'Верхняя одежда':
		OuterwearSelect = f"SELECT * FROM Outerwear WHERE category2 = '{product}'"

		cursorF.execute(OuterwearSelect)
		SelectedList = cursorF.fetchall()


	elif choise == 'Штаны':
		PantsSelect = f"SELECT * FROM Pants WHERE category2 = '{product}'"

		cursorF.execute(PantsSelect)
		SelectedList = cursorF.fetchall()

	return SelectedList









