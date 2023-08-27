#methods: mean two functio that are inside the classes
class item:
    def Calculates_total_price(self, x, y):
        return x * y

item1 = item()
item1.name = 'phone'
item1.price  = 1000
item.quantity = 4
print(item1.Calculates_total_price(item1.price, item1.quantity))
