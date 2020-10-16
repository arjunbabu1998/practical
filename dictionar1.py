limit=int(input("enter the limit"))
my_dict={}
for i in range(0,limit):
    key=int(input("enter the key value: "))
    val=int(key)**2
    my_dict[key]=val
print(my_dict)