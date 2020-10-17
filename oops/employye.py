class Employee:
    def __init__(self):
        self.exp=4
    def putdetail(self,na,sa,jo):
        self.name=na
        self.salary=sa
        self.job=jo
    def getdetail(self):
        print("Name = %s" % self.name)
        print("Salary = %s" % self.salary)
        print("Job = %s" % self.job)
        print("Experience = %s" % self.exp)

detail=Employee()
detail.putdetail('Arjun',48000,'Python Developer')
detail.getdetail()