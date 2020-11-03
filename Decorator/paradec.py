def divide(func):
    def inner(a,b):
        if (b==0):
            return("Can't divide")
        else:
            return(func(a,b))

        return func(a, b)
    return inner


@divide
def divide(a,b):
    return(a/b)

a=int(input("enter the first value : "))
b=int(input("enter the second value : "))

print(divide(a,b))