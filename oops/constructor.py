class Training:
    def __init__(self,name,rlno):
        print("In constructor")
        self.name=name
        self.rlno=rlno
    def display_details(self):
        print("Name is :",self.name)
        print("Roll number is :",self.rlno)

obj1=Training('Arjun',200)
obj1.display_details()

print("_____________________")

obj2=Training('Anjana',390)
obj2.display_details()