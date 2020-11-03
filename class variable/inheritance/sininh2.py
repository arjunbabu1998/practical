class Person:
    def __init__(self,name,place):
        self.name=name
        self.place=place
    def show(self):
        print(self.name,self.place)

class Student(Person):
    def __init__(self,rlno,name,place):
        self.name=name
        self.rlno=rlno
        self.place=place
    def display(self):
        print(self.name,self.rlno,self.place)

s=Student(12,'Arjun','ktm')
s.show()
s.display()