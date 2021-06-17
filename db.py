
import sqlite3 as sql



class DBWorker:
    def __init__(self, db_name):
        self.cur_db = sql.connect(db_name)
        self.cursor = None
        self.result = None

    def connect_db(self):
        self.cursor = self.cur_db.cursor()
    
    def use_query(self, query):
        self.cursor.execute(query)
        self.result = self.cursor.fetchall()
        self.cur_db.commit()

    def return_result(self):
        return self.result


db = DBWorker('new_some.db')
db.connect_db()
db.use_query("CREATE TABLE shop (id integer PRIMARY KEY, name varchar(60), location varchar(100));")
# db.use_query("CREATE TABLE product (id integer PRIMARY KEY, name varchar(60), cost float, shop_id integer);")
# 
# db.use_query('INSERT INTO shop(name, location) VALUES("EVROOPT", "MINSK")')

# db.use_query('INSERT INTO product(name, cost, shop_id) VALUES("milk", 10, 1)')
# db.use_query('INSERT INTO product(name, cost, shop_id) VALUES("papper", 10.0, 1)')

# db.use_query('INSERT INTO product(name, cost, shop_id) VALUES("milk", 10, 100)')
# db.use_query('INSERT INTO product(name, cost, shop_id) VALUES("papper", 10.0, 200)')

query = 'DELETE FROM product WHERE shop_id!=1;'


db.use_query(query)
# db.use_query('SELECT name, cost FROM product ORDER BY cost')
db_values = db.return_result()

print(db_values)

query = 'SELECT * FROM shop;'


db.use_query(query)
# db.use_query('SELECT name, cost FROM product ORDER BY cost')
db_values = db.return_result()

print(db_values)
# import pdb; pdb.set_trace()
