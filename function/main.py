def sum(num1, num2):
    if type(num1) != type(num2):
        print('please give the number same type')
        return
    return (num1 + num2)

print(sum(15, 14))
print(sum('hello', 'jkdj'))
print(sum('hsks', 234))


#function with arguments or default arguments
#function with paramter
def student(name = 'fjjfj', age = 00):
    print('name: ', name)
    print('age: ', age)

#defim=ne mutiple argument  with (*)
def student(name, age, *marks):
    print('name: ', name)
    print('age: ', age)
    print('maks: ', marks)
student('tom',22, 34, 56, 44)

#you can provide the key value pairs as a marks arguments with(**)
def student(name, age, **marks):
    print('name: ', name)
    print('age: ', age)
    print('maks: ', marks)
student('tom',22, english = 34, physic = 56, biology = 44)
