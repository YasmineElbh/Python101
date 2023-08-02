print('ma Bank')

pin = int(input('enter yur pin: '))

while pin != 1234:
    pin = int(input('incorrect pin'))

if pin == 1234:
    print('pin accepted!')


#guessing number

tries = 0
guess = 0

while guess != 6 and tries < 3:
    print(int(input('guess the number! ')))
    tries = tries + 1

if guess != 6 and tries:
    print('you ran out of tries')
else:
    print('bravo! you got it')