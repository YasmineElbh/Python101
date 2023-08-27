class Student:
    no_of_student = 0
    def __init__(self, name, age = 0, courses = 'none'):
        self.name = name
        self.age = age
        self.courses = courses
        #we can make the value attribut private like this
        #self.__name = name
        #self.__age = age
        #number of students
        Student.no_of_student += 1
#class methods
#instends method(make acces to the parameters)

    def describe(self):
        # print(f"my name is {self.name} and my age is {self.age}")
        # print(f"my name is {self.__name} and my age is {self.__age}")
        print("my name is {} and my age is {}".format(self.name, self.age))
#get && set(encapsulation)
    def get_name(self):
        return self.name
        #return self.__name
    def set_name(self, new_name):
        self.name = new_name
        #self.__name = new_name
    def is_old(self,num):
        if self.age <= num:
                print("student is old")
        else:
                print("student is not old")

student1 = Student("yasmine", 66, ['science'])
student2 = Student("ydd", 60, ['cs', 'design'])
#print(student1.age, student2.name)
#change
# student1.name = "dodo"
# student1.age = 77
# print(student1.age, student1.name)
# print(student2.no_of_student)
# student1.describe()

student1.is_old(50)

print(student1.get_name())
student1.set_name("aaaa")
print(student1.get_name())