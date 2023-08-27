#staticMethod: don;t take self parameters or insteds method and can not change attribut oor class object

class Math:
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def add5(num):
        return num + 5
    
    @staticmethod
    def PI():
        return 3.14

#another example
class Pizza:
    def __init__(self, radius, ingredient):
        self.radius = radius
        self.ingredients = ingredient

    def __str__(self):
        return f'pizza ingredients are {self.ingredients}'

    def area(self):
        return Pizza.circle_area(self.radius)
                
@staticmethod
def circle_area(r):
    return r ** 2 * Math.PI()
        
# x = Math.add(5, 10)
# y = Math.add5(x)
# print(x, y)

p = Pizza(6, ['mozarilla', 'tomatoes'])
print(p.area())
print(Pizza.circle_area(4))