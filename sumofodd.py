numbers=[1,2,3,4,5,6,7,8,9]
print(numbers)
for i in numbers:
    if i%2==0:
        numbers.remove(i)
print(numbers)