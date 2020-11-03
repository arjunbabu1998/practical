class Circle:
    def __init__(self,rad):
        self.rad=rad

    def area(self):
        cirarea=3.14*(self.rad*self.rad)
        return(cirarea)

    def perimeter(self):
        peri=2*3.14*self.rad
        return(peri)

class Cone(Circle):
    def __init__(self,rad,height):
        super().__init__(rad)
        self.height=height

    def volume(self):
        vol=(1/3)*(super().area())*self.height
        return(vol)

rad=int(input("Enter the radious of the circle"))
height=int(input("Enter the height of the cone"))
obj=Cone(rad,height)
obj.area()
print("Circle Area = ",obj.area())
obj.perimeter()
print("Circle Perimeter = ",obj.perimeter())
obj.volume()
print("Volume of the Cone = ",obj.volume())
