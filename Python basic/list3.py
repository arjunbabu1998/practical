limit=int(input("enter the number of elements"))
liststore=[]
sumof=0
for i in range(1,limit+1):
    values=int(input("enter the values"))
    liststore.append(values)
sumof=sumof+i
print("sum=%d" % sumof)