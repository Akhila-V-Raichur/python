import math
class shape:
    def __init__(self):
        self.name=""
        self.area=0
    def showarea(self):
        print("the area of",self.name,"is",self.area,"units")
class circle(shape):
    def __init__(self,radius):
        self.area=0
        self.name="circle";
        self.radius=radius
    def calcarea(self):
        self.area=math.pi*self.radius*self.radius

c1=circle(5)
c1.calcarea()
c1.showarea()