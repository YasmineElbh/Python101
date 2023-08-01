#Create a currency.py program that asks the user for the amount they have in peso, soles, and reais and calculates the total in USD.

pesos = int(input('What do you have left in pesos? '))
reais = int(input('What do you have left in reais? '))
soles = int(input('What do you have left in soles? '))

total = pesos * 0.058 + soles * 0.28 + reais * 0.21
print('the total is: ', total)