class car:
    def __init__(self, speed,color):
        #print(speed)
        #print(color)
        self.speed = speed
        self.color = color
       # print('the __init__ is called')

porche = car(200, 'blue')
mercedessClass = car(350, 'black')
jeep = car(400, 'black')

print(porche.speed)
print(jeep.color)


