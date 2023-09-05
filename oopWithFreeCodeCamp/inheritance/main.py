class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        print('food is created from base class')
    def eat(self):
        print('eat method from base class')

class Apple(Food): #devired class
    def __init__(self, name, price):
        #Attribut name
        # self.name = name
        Food.__init__(self, name, price) #create instance from base class
        super().__init__(name, price)
        self.price = price + 20
        self.name = name
        #print('Apple is created from derived class')
        print(f'{self.name} Apple is created from derived class and price is {self.price}')

food1 = Apple('ypoo',150)
food1.eat()