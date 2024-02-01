from db import Db

class Product:
    def __init__(self):
        self.table = 'product'
        self.db = Db(host="localhost", user="root", password="patesaup0ulet", database="store")

    def create(self, name, description, price, quantity, id_category):
        query = f"INSERT INTO {self.table} (name, description, price, quantity, id_category) VALUES (%s, %s, %s, %s, %s)"
        params = (name, description, price, quantity, id_category)
        self.db.executeQuery(query, params)

    def read(self):
        query = f"SELECT * FROM {self.table}"
        return self.db.fetch(query)
    
    def update(self, id, price, quantity):
        query = f"UPDATE {self.table} SET price = %s, quantity = %s WHERE id = %s"
        params = (price, quantity, id)
        self.db.executeQuery(query, params)

    def delete(self, id):
        query = f"DELETE FROM {self.table} WHERE id = %s"
        params = (id,)
        self.db.executeQuery(query, params)

    def readOne(self, id):
        query = f"SELECT * FROM {self.table} WHERE id = %s"
        params = (id,)
        return self.db.fetch(query, params)
    
    def readByCategory(self, id_category):
        query = f"SELECT * FROM {self.table} WHERE id_category = %s"
        params = (id_category,)
        return self.db.fetch(query, params)
