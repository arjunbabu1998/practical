class Training:

    def __init__(self,name,rlno):
        print("In constructor")
        self.name=name
        self.rlno=rlno
    def display_details(self):
        print"Name is : ",self.name)
        print("roll number: ",self.rlno)

obj=Training('Arjun',110)
obj1.display_details()

print("_____________________________")

obj2=Training('Anjana',120)
obj2.display_details()