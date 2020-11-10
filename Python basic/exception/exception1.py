try:
    a=int(input("Enter first number to be divided : "))
    b=int(input("Enter second number to divide : "))
    res=a/b
    print("Result = ",res)
except Exception:
    res=0
    print("division is not possible by zero")
else:
    print("Program success")
finally:
    print(res)
    print("The end: ")

#or

#try:
    #a=int(input("Enter first number to be divided : "))
    #b=int(input("Enter second number to divide : "))
    #res=a/b
    #print("Result = ",res)
#except zeroDivisionError as e:
    #res=0
    #print(e)
#else:
    #print("Program success")
#finally:
    #print(res)
    #print("The end: ")

