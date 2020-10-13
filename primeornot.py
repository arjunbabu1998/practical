num=int(input("Enter any number "))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print(" %d is not a prime number " % num)
            break
    else:
        print(" %d is a prime number " % num)
else:
    print(" %d is not a prime number " % num)