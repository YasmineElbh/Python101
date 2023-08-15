#A tuple is an immutable object, which means it cannot be changed, and we use it to represent fixed collections of items
#A tuple is a collection of immutable Python objects. It can hold elements of any arbitrary data type (integer, string, float, list, etc.)

x = (1, 4, 4, 5)
x.count(4)

y = (1, 'jfj', 0)
z = x + y

a = ('hiii') * 5

max(x) #the maximum value stored in the tuple
min(x)
del y