radious=float(input("enter the radious of cone : "))
height=float(input("enter the height of cone : "))
result=lambda radious,height:((3.14*radious)**2)*(height/3)
print("Volume= ",result(radious,height))