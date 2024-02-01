from product import Product
from category import Category

class Shop:
    def __init__(self):
        self.product = Product()
        self.category = Category()

    def createProduct(self, name, description, price, quantity, id_category):
        self.product.create(name, description, price, quantity, id_category)

    def readProducts(self):
        return self.product.read()
    
    def updateProduct(self, id, price, quantity):
        self.product.update(id, price, quantity)

    def deleteProduct(self, id):
        self.product.delete(id)

    def createCategory(self, name):
        self.category.create(name)

    def readCategories(self):
        return self.category.read()
    
    def updateCategory(self, id, name):
        self.category.update(id, name)

    def deleteCategory(self, id):
        self.category.delete(id)

    def readOneCategory(self, id):
        return self.category.readOne(id)
    
    def readOneProduct(self, id):
        return self.product.readOne(id)
    
    def readByCategory(self, id_category):
        return self.product.readByCategory(id_category)

    