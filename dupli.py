num=[10,20,30,10,10,20,5]
for x in num:
    count=0
    for j in num:
        if(x==j):
          count=count+1
          if(count>1):
              num.remove(x)

    #print(count)
print(num)

