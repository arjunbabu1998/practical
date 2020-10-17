limit=int(input("enter the limit"))
my_dict={}
for i in range(0,limit):
    key=input("enter the key value: ")
    val=input("enter the value: ")
    my_dict[key]=val
print(my_dict)