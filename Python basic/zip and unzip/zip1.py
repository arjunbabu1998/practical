names=["Arjun","Vishnu","Tins","Sibin"]
rollnumber=[1,2,3,4]
marks=[21,22,23,24]

mapped=zip(names,rollnumber,marks)
mapped=list(mapped)

print("The zipped rsult is : ",end="")
print(mapped)

#for unzipping

names,rollnumber,marks=zip(*mapped)

print("Unzipped list is : ")

print("Unzipped names in the list is :",end="")
print(names)

print("Unzipped roll numbers in th list is :",end="")
print(rollnumber)

print("Unzipped mark in the list is :",end="")
print(marks)