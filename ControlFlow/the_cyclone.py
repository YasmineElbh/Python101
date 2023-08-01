#Ask the user what their height is and how many credits they have using the int() and input() functions. Make sure to store the values in a height variable and a credits variable.

height = int(input('what is your height ' ))
creditss = int(input('how many credits you have?'))

if height == 190 and creditss == 250:
    print('enjoy the ride!')
elif height < 190 and creditss == 250:
    print('You are not tall enough to ride')
elif height == 190 and creditss != 250:
    print('You dont have enough credits.')
else:
    print('you are nt tall enought and you dont have a credits enought')