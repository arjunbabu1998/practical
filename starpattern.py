rows=int(input("enter the number for * pattern: "))
for i in range(rows+1,0,-1):
    for j in range(0,i-1):
        print("*",end='')
    print("")