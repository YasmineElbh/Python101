#methods: mean two functio that are inside the classes
#__init__:is a method with a unique name that you need to call it the way it is intentionally in order to use its special futures
#self: allow to assign the attributes from the init method

class item:
    def __init__(self, name, price, quantity):
    #  print(f'An instence created: {name}')
        self.name = name
        self.price = price
        self.quantity = quantity
    def Calculates_total_price(self):
        return self.price * self.quantity


item1 = item("sams", 100, 5)
# item1.price  = 1000
# item.quantity = 4
#print(item1.Calculates_total_price(item1.price, item1.quantity))
print(item1.name)
print(item1.price)