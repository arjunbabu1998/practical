#fp=open("sample3.txt","w")
#l1=['Arjun \n','Babu\n','Padiyappallil\n']
#fp.writelines(l1)
#fp.close()

#or

with open("sample3.txt","w") as fp:
    fl1=["Arjun \n","Babu\n","Padiyappallil\n"]
    fp.writelines(l1)