#import random usd to generate random number i python
#For example, random.randint(0, 10) will return a random number from [0, 1, 2, 3, 4, 5, 6, 7, 8 ,9, 10].
#random.randint:returns a random integer between the higher and lower limit passed as parameters

import random

num = random.randint(0, 10)

if num > 20:
    print('heads')
else:
    print('tails')