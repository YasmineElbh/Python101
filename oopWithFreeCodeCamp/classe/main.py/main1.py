#instance attribut: which are defined in the __init__() function and are somewhat dynamic because they can have different values in each object.
#Class attribut: remain the same for every object and are defined outside the __init__()
#assert: is a statement keyword that is used t chec if there is a match between what is happening to your expectations

class item:
    pay_rate = 0.8
    def __init__(self, name: str, price: float, quantity = 0):
        #Run validation to the received argument
        assert price >= 0, f'price{price} is not greater than zero'
        assert quantity >= 0
        
        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def Calculates_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * item.pay_rate

item1 = item("sams", 100, 5)
item2 = item("sas", 200, 3)

# print(item1.Calculates_total_price())
# print(item2.Calculates_total_price())
print(item1.pay_rate)
print(item.__dict__) #all the attributes for class level 
print(item1.__dict__) #all the attributes for instance level 


item1.apply_discount()
print(item1.price)
