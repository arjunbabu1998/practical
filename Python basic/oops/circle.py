class circle:
    
    def __init__(self,rad):
        self.rad=rad

    def area(self):
        return(3.14*self.rad*self.rad)

    def perimeter(self):
        return(2*3.14*self.rad)

obj=circle(5)
print("Area is :",obj.area())
print("Perimeter is :",obj.perimeter())