fp=open("second_sample.txt","w")
fp.write("Spectrum Solutions")
fp.close()

with open("second_sample.txt","r") as fp:
    print(fp.read())