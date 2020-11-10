def file_write(fname,data):
    fp=open(fname,"w")
    fp.write(data)
    fp.close()

fname="third_sample.txt"

data="Arjun"

#fp=open("second_sample.txt","w")
#fp.write("Spectrum Solutions")
#fp.close()

#with open("second_sample.txt","r") as fp:
#    print(fp.read())