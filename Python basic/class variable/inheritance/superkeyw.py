class Person:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def display(self):
        print(self.id,self.name)

class Student(Person):
    def __init__(self,id,name,mark):
        super().__init__(id,name)
        self.mark=mark

    def show(self):
        super().display()
        print(self.id,self.name,self.mark)

s=Student(12,'Arjun',50)
s.display()
s.show()