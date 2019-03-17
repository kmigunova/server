class UsersModel:
    def __init__(self, connection):
        self.connection = connection

    def init_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                             user_name VARCHAR(20) UNIQUE,
                             password_hash VARCHAR(128),
                             email VARCHAR(20),
                             is_admin INTEGER
                             )''')
        cursor.close()
        self.connection.commit()

    def insert(self, user_name, password_hash, email, is_admin=False):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO users 
                          (user_name, password_hash, email, is_admin) 
                          VALUES (?,?,?,?)''',
                       (user_name, password_hash, email, int(is_admin)))
        cursor.close()
        self.connection.commit()

    def exists(self, user_name):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE user_name = ?", [user_name])
        row = cursor.fetchone()
        return (True, row[2], row[0]) if row else (False,)

    def get(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (str(user_id)))
        row = cursor.fetchone()
        return row

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        return rows


class AccessoriesModel:
    def __init__(self, connection):
        self.connection = connection

    def init_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS accessories 
                            (acs_id INTEGER PRIMARY KEY AUTOINCREMENT,
                             price INTEGER,
                             type VARCHAR(100)
                        )''')
        cursor.close()
        self.connection.commit()

    def insert(self, price, type):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO accessories 
                          (price, type) 
                          VALUES (?,?,?,?,?)''',
                       (str(price), type))
        cursor.close()
        self.connection.commit()

    def exists(self, model):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM accessories WHERE model = ?",
                       model)
        row = cursor.fetchone()
        return (True, row[0]) if row else (False,)

    def get(self, acs_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM accessories WHERE car_id = ?", (str(acs_id)))
        row = cursor.fetchone()
        return row

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT price, acs_id FROM accessories")
        rows = cursor.fetchall()
        return rows

    def delete(self, acs_id):
        cursor = self.connection.cursor()
        cursor.execute('''DELETE FROM accessories WHERE acs_id = ?''', (str(acs_id)))
        cursor.close()
        self.connection.commit()

    def get_by_price(self, start_price, end_price):
        cursor = self.connection.cursor()
        cursor.execute("SELECT price, acs_id FROM accessories WHERE price >= ? AND price <= ?",
                       (str(start_price), str(end_price)))
        row = cursor.fetchall()
        return row
