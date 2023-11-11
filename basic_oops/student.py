# simple inheritance

# there will be a parent class and a child class, the parent class will be called and applied to the child class

# parent class
class Teenager(object):

    # the constructor
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    # the methods
    def display(self):
        print(self.name)
        print(self.student_id)

    def details(self):
        print("My name is " + self.name)
        print("My student id is " + str(self.student_id))
    
# child class 
class Student(Teenager):
    
    def __init__(self, name, student_id, grade, faction):
        self.grade = grade
        self.faction = faction

        # invoking or calling on __init__ (constructor) of the parent class
        Teenager.__init__(self, name, student_id)

    def details(self):
        print("My name is " + self.name)
        print("My student id is " + str(self.student_id))
        print("The grade I am currently in is " + str(self.grade))
        print("The faction I am apart of is " + self.faction)

# creation of an object variable or an instance
s1 = Student('Johnny', 3694199, 11, 'McAdam')

s1.display()
print('-')
s1.details()

# notes:
# the reason behind having a details method in both the parent and child class is due to setting the stage with the parent class having a defaulted details method 
# that can be inherited by the child class if an object is instantiated using the child class in lieu of the parent class.
# This oop concept of inheritance shown here provides the child class with the flexibility to utilise the defaulted details method if it doesnt want to create it own version, 
# but also has the option to still create it own version of the details class which will then be overriden, granted that the object created used the child class type instead of 
# the parent class type.
# This I believe in essence is the beauty of the inheritance concept in OOP.