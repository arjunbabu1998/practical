number=int(input("enter any number"))
real=number
ans=0
while number>0:
    temp=number%10
    ans=ans+(temp*temp*temp)
    number=int(number/10)
    
if ans==real:
    print("%d is an armstrong number" % real)
else:
    print(" %d is not an armstrong number" % real)
