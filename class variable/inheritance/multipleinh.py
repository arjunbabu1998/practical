class Teacher1:

    def __init__(self,name1,age1):
        self.name1=name1
        self.age1=age1

    def display1(self):
        print(self.name1,self.age1)

class Teacher2:

    def __init__(self,name2,age2):
        self.name2=name2
        self.age2=age2

    def display2(self):
        print(self.name2,self.age2)

class Student(Teacher1,Teacher2):

    def __init__(self,name1,age1,name2,age2,mark1,mark2):
        Teacher1.__init__(self,name1,age1)
        Teacher2.__init__(self,name2,age2)
        self.mark1=mark1
        self.mark2=mark2
    def display3(self):
        print(self.name1,self.age1,self.name2,self.age2,self.mark1,self.mark2)

s=Student('Arjun',22,'Anjana',18,55,50)
s.display1()
s.display2()
s.display3()