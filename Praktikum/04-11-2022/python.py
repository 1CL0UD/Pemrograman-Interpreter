class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self):
        return self.x+self.y
    #setter getter
    def getX(self):
        return self.x
    def setX(self, x):
        self.x = x
    def getY(self):
        return self.y
    def setY(self, y):
        self.y = y

p1 = MyClass(5, 6)

# print(p1.x)
# print(p1.y)

print(p1.sum())