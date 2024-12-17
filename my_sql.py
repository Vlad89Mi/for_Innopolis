import sqlite3
import os
import sys
import pandas 

connection  = sqlite3.connect('USERS.db')
cursor  = connection .cursor()

def table_exists(table_name): 
    cursor.execute('''SELECT count(name) FROM sqlite_master WHERE TYPE = 'table' AND name = '{}' '''.format(table_name)) 
    if cursor.fetchone()[0] == 1: 
        return True 
    return False

if not table_exists('USERS'): 
    cursor.execute(''' CREATE TABLE USERS ( 
                   id INTEGER NOT NULL PRIMARY KEY, 
                   FIO  TEXT NOT NULL,
                   gift TEXT NOT NULL,
                   price INTEGER NOT NULL, 
                   buy TEXT NOT NULL ); ''')
else: 
    print('Удаление уже созданой таблицы завершено.')
    connection.close()
    os.remove('USERS.db')
    sys.exit()

query = 'INSERT INTO USERS (id, FIO, gift, price, buy) values(?, ?, ?, ?, ?)'
data = [ 
    ( 1  , 'Поздняков Владимир Маркович' , 'Комплект косметических средств' , 2393 , 'куплен' ),
    ( 2  , 'Морозов Александр Ярославович' , 'Страховка на путешествие' , 1848 , 'не куплен' ),
    ( 3  , 'Горюнова Ксения Андреевна' , 'Семейный фотоальбом' , 2435 , 'не куплен' ),
    ( 4  , 'Осипов Артём Эминович' , ' одарочная карта для онлайн-магазина' , 8193 , 'куплен' ),
    ( 5  , 'Кириллова Ева Артёмовна' , 'Набор для путешествий' , 1016 , ' куплен ' ),
    ( 6  , 'Любимова Александра Михайловна' , 'Подписка на стриминговый сервис' , 7264 , 'не куплен' ),
    ( 7  , 'Гришина Александра Егоровна' , 'Подушка с необычным дизайном' , 10024 , 'не куплен' ),
    ( 8  , 'Попова Анастасия Святославовна' , 'Велосипед' , 1106 , 'куплен' ),
    ( 9  , 'Макаров Тимофей Максимович' , 'Набор для приготовления кофе' , 1903 , 'куплен' ),
    ( 10 , 'Волков Леонид Давидович' , 'Электросамокат' , 13574 , 'куплен' ),
    ( 11 , 'Артемова Елизавета Кирилловна' , 'Уникальный магнитик на холодильник' , 7848 , 'куплен' ),
    ( 12 , 'Тихомиров Константин Кириллович' , 'Книга интересного автора' , 11410 , 'не куплен' ),
    ( 13 , 'Карасев Родион Даниилович' , 'Ароматические свечи для дома' , 5482 , 'куплен' ),
    ( 14 , 'Осипова Милана Тимуровна' , 'Электрический чайник или кофеварка' , 5296 , 'куплен' ),
    ( 15 , 'Медведев Семён Артёмович' , 'Шарф из натуральных материалов' , 4624 , 'куплен' ),
    ( 16 , 'Гаврилова Виктория Дмитриевна' , 'Комплект ручек разных цветов' , 9266 , 'не куплен' )
   ]

with connection:
    connection.executemany(query, data)

print('Добавлено строк в базу:', connection.total_changes)
print('База данных готова.')
connection.commit()

records = '''SELECT * FROM USERS'''
cursor.execute(records)
dataframe = pandas.read_sql_query(records, connection)
connection.close()
dataframe = dataframe.rename(columns={'FIO': 'ФИО', 'gift': 'Подарок', 'price' : 'Цена', 'buy' : 'Статус'})
print(dataframe)