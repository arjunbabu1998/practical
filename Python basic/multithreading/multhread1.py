from _thread import start_new_thread
import time

def print_time(mystr,delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s:%s" % (mystr,time.ctime(time.time())))

#print_time("hello",2)
#print_time("hi",2)
try:
    start_new_thread(print_time, ("Hello",2,))
    start_new_thread(print_time, ("Hi",2,))
except:
    print("error : unable to start thread")

while 1:
    pass
