for x in range(1, 100):
    #print(x)
    if (x % 3 == 0 and x % 5 == 0):
        print('fizzbuzz')
    elif (x % 5 == 0):
        print('buzz')
    elif (x % 3 == 0):
        print('fizz')
    else:
        print(x)