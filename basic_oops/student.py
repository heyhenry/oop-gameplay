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
