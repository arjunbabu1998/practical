import time

print(time.time())
now = time.localtime(time.time())
print(now)

print("asctime",time.asctime(now))

print(time.strftime("%m-%d-%y : %H:%M:%S",now))

print("strftime",time.strftime("%a %b %d",now))

print(time.strftime("%c",now))

print("UUUUUU",time.strftime("%Y-%m-%d %H:%M:%S %Z %p %P",now))