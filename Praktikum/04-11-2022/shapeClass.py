class shape:
    def __init__ (self, x, y):
        self.x=x
        self.y=y
    def area(self):
        return self.x*self.y/2
    def perim(self):
        return self.x*3

Obj = shape(3,4)

print("%.2f" %Obj.area())
print("%.2f" %Obj.perim())