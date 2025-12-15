class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def discount(self, percent):
        self.price -= self.price * percent / 100

    def sell(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount

    def __str__(self):
        return f"{self.name} | Narx: {self.price} | Soni: {self.quantity}"


product = Product("Noutbuk", 8000000, 5)
product.discount(20)
product.sell(2)
print(product)
