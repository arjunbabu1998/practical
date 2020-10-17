class Student:
    def __init__(self):
        self.grace=20
    def setmark(self,m1,m2):
        self.mrk1=m1
        self.mrk2=m2
    def getmark(self):
        total=self.mrk1+self.mrk2+self.grace
        print("Total= %d " % total)

progress=Student()
progress.setmark(20,30)
progress.getmark()