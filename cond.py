number=int(input("enter any limit: "))
for i in range(0,number):
    if i%7==0 and i%5!=0:
        print(i)