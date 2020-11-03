class Person:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(self.name)

class Student(Person):
    pass

s=Student('Arjun')
s.show()