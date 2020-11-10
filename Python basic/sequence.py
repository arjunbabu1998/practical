n=int(input("enter the number"))
mul=1
numbers=[n]
print(numbers)
for x in range(0,n-1):
    last=numbers[-1]
    mul=mul*10
    new=mul*n
    new=new+last   
    numbers.append(new)

print(numbers)
print(sum(numbers))
    
    

    