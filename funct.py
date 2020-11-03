def showNumbers(limit):
    for i in range(0,limit):
        if i%2==0:
            print(i ,"is even")
        else:
            print(i ,"is odd")

limit=int(input("enter the limit"))
showNumbers(limit)      