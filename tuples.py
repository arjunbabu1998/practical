tup1=('phy','che',97,20)
tup2=(1,2,3,4,5,6,7)
print(tup1[1:4])
print(tup2[-4:-1])
tup3=list(tup1)
print(type(tup3))
for i in tup1:
    print(i)

if 'phy' in tup1:
    print("yes phy is in this tuples")

print(len(tup2))
tup4=tup1+tup2
print(tup4)
print(max(tup2))
print(min(tup2))