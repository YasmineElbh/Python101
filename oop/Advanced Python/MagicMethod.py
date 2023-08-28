from typing import Any


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #delete object
    def __del__(slef):
        print('objects is being deleted')

p = Person('Mmmmm', 34)

#another example
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #adding
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    #representing
    def __repr__(self):
        return f"X: {self.x}, Y: {self.y}" 

    def __call__(self):
        print("Hello i was called!")

v1 = Vector(10, 10)
v2 = Vector(40, 40)
v3 = v1 + v2
print(v3)
v3()
