#assert: is a statement keyword that is used t chec if there is a match between what is happening to your expectations
class item:
    def __init__(self, name: str, price: float, quantity = 0):
        #Run validation to the received argument
        assert price >= 0
        assert quantity >= 0
        
        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def Calculates_total_price(self):
        return self.price * self.quantity


item1 = item("sams", 100, 5)
item2 = item("sas", 200, 3)

print(item1.Calculates_total_price())
print(item2.Calculates_total_price())

