import sqlite3 as sq


#cursorM = connectionM.cursor()
#cursorF = connectionF.cursor()

ShoesCreateTable = "CREATE TABLE Shoes(category2 text, photo text, name text primary key, price text)"
OuterwearCreateTable = "CREATE TABLE Outerwear(category2 text, photo text, name text primary key, price text)"
PantsShoesCreateTable = "CREATE TABLE Pants(category2 text, photo text, name text primary key, price text)"
AccessoriesCreateTable = "CREATE TABLE Accessories(category2 text, photo text, name text primary key, price text)"

connectionM = sq.connect('MaleDB.db')
connectionF = sq.connect('FemaleDB.db')



def sql_male(data):
	connectionM = sq.connect('MaleDB.db')

	if data['category1'] == 'Аксессуары':
		AccessoriesInsertTable = f"INSERT INTO Accessories(category2, photo, name, price) VALUES ('{data['category2'][7:]}', '{data['photo']}', '{data['name']}', '{data['price']}')"
		connectionM.execute(AccessoriesInsertTable)

	elif data['category1'] == 'Обувь':
		ShoesInsertTable = f"INSERT INTO Shoes(category2, photo, name, price) VALUES ('{data['category2'][7:]}', '{data['photo']}', '{data['name']}', '{data['price']}')"
		connectionM.execute(ShoesInsertTable)

	elif data['category1'] == 'Верхняя одежда':
		OuterwearInsertTable = f"INSERT INTO Outerwear(category2, photo, name, price) VALUES ('{data['category2'][7:]}', '{data['photo']}', '{data['name']}', '{data['price']}')"
		connectionM.execute(OuterwearInsertTable)

	elif data['category1'] == 'Штаны':
		PantsInsertTable = f"INSERT INTO Pants(category2, photo, name, price) VALUES ('{data['category2'][7:]}', '{data['photo']}', '{data['name']}', '{data['price']}')"
		connectionM.execute(PantsInsertTable)

	connectionM.commit()
	connectionM.close()


def sql_female(data):
	connectionF = sq.connect('FemaleDB.db')

	if data['category1'] == 'Аксессуары':
		AccessoriesInsertTable = f"INSERT INTO Accessories(category2, photo, name, price) VALUES ('{data['category2'][7:]}', '{data['photo']}', '{data['name']}', '{data['price']}')"
		connectionF.execute(AccessoriesInsertTable)

	elif data['category1'] == 'Обувь':
		ShoesInsertTable = f"INSERT INTO Shoes(category2, photo, name, price) VALUES ('{data['category2'][7:]}', '{data['photo']}', '{data['name']}', '{data['price']}')"
		connectionF.execute(ShoesInsertTable)

	elif data['category1'] == 'Верхняя одежда':
		OuterwearInsertTable = f"INSERT INTO Outerwear(category2, photo, name, price) VALUES ('{data['category2'][7:]}', '{data['photo']}', '{data['name']}', '{data['price']}')"
		connectionF.execute(OuterwearInsertTable)

	elif data['category1'] == 'Штаны':
		PantsInsertTable = f"INSERT INTO Pants(category2, photo, name, price) VALUES ('{data['category2'][7:]}', '{data['photo']}', '{data['name']}', '{data['price']}')"
		connectionF.execute(PantsInsertTable)

	connectionF.commit()
	connectionF.close()
