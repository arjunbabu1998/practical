class Methods:
    def testfun(self):
        print("Normal function")

    @classmethod
    def myclassmethod(cls):
        print("in class method")

    @staticmethod
    def mystaticmethod(a,b):
        print("in static method",a,b)

obj=Methods()
obj.testfun()
obj.myclassmethod()
obj.mystaticmethod(20,30)

print("_________________")

Methods.myclassmethod()
Methods.mystaticmethod(10,40)


    
        