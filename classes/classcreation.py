class Firstclass:
    def __init__(self):
        print("In constructor")
    def python(self,name,rlno):
        print("in python class  ")
        self.name=name
        self.rlno=rlno
    def django(self,name,rlno):
        print("in django class  ")
        self.name=name
        self.rlno=rlno
    def datascience(self,name,rlno):
        print("in data science class  ")
        self.name=name
        self.rlno=rlno
obj=Firstclass('Arjun',1)
obj.python()
obj.django()

obj1=Firstclass('Anjana',2)
obj1.python()
obj1.django()

obj2=Firstclass('akshay',3)
obj2.python()
obj2.datascience()
