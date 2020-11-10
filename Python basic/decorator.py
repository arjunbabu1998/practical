def msg(fun):
    def show():
        print('welcome')
        fun()
    return show

@msg
def f1():
    print('tins')

@msg
def f2():
    print('arjun')


f1()
f2()