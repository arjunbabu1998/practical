limit= int(input("ente the limit of first set : "))
set1=set()
set2=set()
set3=set()
for i in range(0,limit):
    item=int(input("enter the elements : "))
    set1.add(item)
print("first set: ",set1)

limit= int(input("ente the limit os the second set : "))
set2=set()
for i in range(0,limit):
    item=int(input("enter the elements : "))
    set2.add(item)
print("second set: ",set2)

set3=set1-set2
print("set difference : ",set3)