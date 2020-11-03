def employee(name,salary=None):
    print("Name= %s" % name)
    if salary:
        print("Salary= %d" % salary)
    else:
        print("salary is less than 9000")
name=str(input("enter the name"))
salary=int(input("enter the salary"))
#employee(name,salary)
employee(name)