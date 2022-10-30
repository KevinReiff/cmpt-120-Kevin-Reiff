class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def inStock(self, quantity):
        return self.quantity >= quantity

    def getStock(self):
        return self.quantity

    def getTotalCost(self):
        return self.quantity * self.price

    def remove(self, quantity):
        self.quantity = self.quantity - quantity
    
    


    