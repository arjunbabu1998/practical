def decor(func):
    def inner():
        print("Hi,Hello,Welcome")
        print("Spectrum Softech Solutions")
        func()
    return inner
@decor       
def f1():
    print("Inside fun 1")
@decor
def f2():
    print("Inside fun 2")
@decor
def f3():
    print("Inside fun 3")

f1()
f2()
f3()