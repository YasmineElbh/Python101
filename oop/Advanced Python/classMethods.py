#decorators:technique use to modify on functions it;s different fron instends class it tooks  the class self as a parameters

from datetime import date
class Student:
    def __init__(self, name, age = 0, courses = 'none'): #constructor function(initialization)
        self.name = name
        self.age = age
        self.courses = courses

    def describe(self):
        print("my name is {} and my age is {}".format(self.name, self.age))

    @classmethod
    def initfromBirthday(cls, name, birthYea):
        return cls(name, date.today().year - birthYea)
    
    class pizza:
        def __init__(self, ingradients):
            self.ingredients = ingradients  
        
        @classmethod
        def veg(cls):
            return cls(['mushrooms', 'olives', 'onions'])
        
        @classmethod
        def margherita(cls):
            return cls(['mozarilla', 'olives'])
        
        #polymorphism
        def __str__(self):
            return f"Pizza ingredients are {self.ingredients}"
        
    pizza1 = pizza(['tomatoes', 'olives'])
    pizza2 = pizza.veg()
    pizza3 = pizza.margherita()
    print(pizza2, pizza3)
    #to show attribut and function(dunder function)
    print(dir(pizza))

# student1 = Student("yasmine", 66, ['science'])
# student2 = Student("ydd", 60, ['cs', 'design'])
# student3 = Student.initfromBirthday("soso", 1998)
# student3.describe()