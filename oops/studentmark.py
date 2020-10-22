class StudentMark:

    def __init__(self,mat,eng,phy,che):
        self.mat=mat
        self.eng=eng
        self.phy=phy
        self.che=che
       

    def total_mark(self):
        self.total=self.mat+self.eng+self.phy+self.che
        print("Total Score= ",self.total)

    def grade(self):
        if self.total>90:
            print("Grade=A")
        elif self.total>80:
            print("Grade=B")
        elif self.total>70:
            print("Grade=C")
        elif self.total>60:
            print("Grade=D")
        else:
            print("Failed")

mat=int(input("Enter the Maths score="))
eng=int(input("Enter the English score="))
phy=int(input("Enter the Physics score="))
che=int(input("Enter the Chemistry score="))

obj=StudentMark(mat,eng,phy,che)
obj.total_mark()
obj.grade()

print(obj.total)
