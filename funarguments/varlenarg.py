def var_arglist(num1,num2,*val):

    print("Tuple is ....",val)
    print(num1)
    print(num2)
    for i in val:
        print(i)
    return

var_arglist(10,20,30,33,45.4,3.4)