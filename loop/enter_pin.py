print('ma Bank')

pin = int(input('enter yur pin: '))

while pin != 1234:
    pin = int(input('incorrect pin'))

if pin == 1234:
    print('pin accepted!')