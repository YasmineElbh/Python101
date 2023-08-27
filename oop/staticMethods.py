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
    
x = Math.add(5, 10)
y = Math.add5(x)
print(x, y)

