class Student:
    div='A'
    def __init__(self,rlno,name):
        self.rlno=rlno
        self.name=name
    def display(self):
        print(self.rlno,self.name)
        print(Student.div)

s=Student(12,'Arjun')
s.display()
print(Student.div)
print(s.div)