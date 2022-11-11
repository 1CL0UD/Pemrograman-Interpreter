class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myFunct(self):
        return "Hi my name is ", self.name, " and I'm ", self.age, "years old"
    
p1 = Person("John", 36)

print(p1.myFunct())