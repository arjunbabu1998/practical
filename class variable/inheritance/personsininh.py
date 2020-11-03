class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        stuname=self.name
        return(stuname)
        stuage=self.age
        return(stuage)

class Student(Person):
    def __init__(self,name,age):
        super().__init__(name,age)

    def display_student():
        stname=self.name
        return(stname)
        stage=self.age 
        return(stage)

name=input("Enter the name of the student : ")
age=int(input("Enter the age of the student : "))

student=Student(name,age)
student.display()
print("Name of the student : ",student.display())
print("Age of the student : ",student.display())
student.display_student()
print("Name of the student : ",student.display_student())
print("Age of the student : ",student.display_student())
