class UsersModel:
    """Сущность пользователей"""
    def __init__(self, connection):
        self.connection = connection

    def init_table(self):
        """Инициализация таблицы"""
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
        """Вставка новой записи"""
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO users 
                          (user_name, password_hash, email, is_admin) 
                          VALUES (?,?,?,?)''',
                       (user_name, password_hash, email, int(is_admin)))
        cursor.close()
        self.connection.commit()

    def exists(self, user_name):
        """Проверка, есть ли пользователь в системе"""
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE user_name = ?", [user_name])
        row = cursor.fetchone()
        return (True, row[2], row[0]) if row else (False,)

    def get(self, user_id):
        """Возврат пользователя по id"""
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (str(user_id)))
        row = cursor.fetchone()
        return row

    def get_all(self):
        """Запрос всех пользователей"""
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        return rows


class DealersModel:
    """Сущность дилерских центров"""
    def __init__(self, connection):
        self.connection = connection

    def init_table(self):
        """Инициализация таблицы"""
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS dealers 
                            (dealer_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                             name VARCHAR(20) UNIQUE,
                             address VARCHAR(128)
                        )''')
        cursor.close()
        self.connection.commit()

    def insert(self, name, address):
        """Добавление дилерского центра"""
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO dealers 
                          (name, address) 
                          VALUES (?,?)''',
                       (name, address))
        cursor.close()
        self.connection.commit()

    def exists(self, name):
        """Поиск дилерского центра по названию"""
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM dealers WHERE name = ?",
                       name)
        row = cursor.fetchone()
        return (True, row[0]) if row else (False,)

    def get(self, dealer_id):
        """Запрос дилерского центра по id"""
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM dealers WHERE dealer_id = ?", (str(dealer_id)))
        row = cursor.fetchone()
        return row

    def get_all(self):
        """Запрос всех дилерских центров"""
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM dealers")
        rows = cursor.fetchall()
        return rows

    def delete(self, dealer_id):
        """Удаление дилерского центра"""
        cursor = self.connection.cursor()
        cursor.execute('''DELETE FROM dealers WHERE dealer_id = ?''', (str(dealer_id)))
        cursor.close()
        self.connection.commit()


class AccessoriesModel:
    """Сущность автомобилей"""
    def __init__(self, connection):
        self.connection = connection

    def init_table(self):
        """Инициализация таблицы"""
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS accessories 
                            (acs_id INTEGER PRIMARY KEY AUTOINCREMENT,
                             price INTEGER,
                             type VARCHAR(100)
                        )''')
        cursor.close()
        self.connection.commit()

    def insert(self, model, price, type, color):
        """Добавление автомобиля"""
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO accessories 
                          (price, type) 
                          VALUES (?,?,?,?,?)''',
                       (str(price), type))
        cursor.close()
        self.connection.commit()

    def exists(self, model):
        """Поиск автомобиля по модели"""
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM accessories WHERE model = ?",
                       model)
        row = cursor.fetchone()
        return (True, row[0]) if row else (False,)

    def get(self, acs_id):
        """Поиск автомобиля по id"""
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM accessories WHERE car_id = ?", (str(acs_id)))
        row = cursor.fetchone()
        return row

    def get_all(self):
        """Запрос всех автомобилей"""
        cursor = self.connection.cursor()
        cursor.execute("SELECT price, acs_id FROM accessories")
        rows = cursor.fetchall()
        return rows

    def delete(self, acs_id):
        """Удаление автомобиля"""
        cursor = self.connection.cursor()
        cursor.execute('''DELETE FROM accessories WHERE acs_id = ?''', (str(acs_id)))
        cursor.close()
        self.connection.commit()

    def get_by_price(self, start_price, end_price):
        """Запрос автомобилей по цене"""
        cursor = self.connection.cursor()
        cursor.execute("SELECT price, acs_id FROM accessories WHERE price >= ? AND price <= ?",
                       (str(start_price), str(end_price)))
        row = cursor.fetchall()
        return row
