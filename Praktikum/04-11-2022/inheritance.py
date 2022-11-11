class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)
    

class Student(Person):
    def __init__(self, fname):
        Person.__init__(self, fname, "test")

x = Student("John")
x.printname()

x = Student("Mike")
x.printname()
 