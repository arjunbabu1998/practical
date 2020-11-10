limit=int(input("enter the limit"))
my_dict={}
sum=0
for i in range(0,limit):
    key=int(input("enter the key value: "))
    val=int(input("enter the value: "))
    my_dict[key]=val
    sum=sum+val
print(my_dict)
print("sum= %d " % sum)