from db import Db

class Category:
    def __init__(self):
        self.table = 'category'
        self.db = Db(host="localhost", user="root", password="patesaup0ulet", database="store")

    def create(self, name):
        query = f"INSERT INTO {self.table} (name) VALUES (%s)"
        params = (name,)
        self.db.executeQuery(query, params)

    def read(self):
        query = f"SELECT * FROM {self.table}"
        return self.db.fetch(query)
    
    def update(self, id, name):
        query = f"UPDATE {self.table} SET name = %s WHERE id = %s"
        params = (name, id)
        self.db.executeQuery(query, params)

    def delete(self, id):
        query = f"DELETE FROM {self.table} WHERE id = %s"
        params = (id,)
        self.db.executeQuery(query, params)

    def readOne(self, id):
        query = f"SELECT * FROM {self.table} WHERE id = %s"
        params = (id,)
        return self.db.fetch(query, params)