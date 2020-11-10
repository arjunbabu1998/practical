import csv

def csv_writer(data,path):

    with open (path,"w") as csv_file:
        writer=csv.writer(csv_file,delimiter=",")
        for line in data:
            writer.writerow(line)

data=["first_name,last_name,city",
            "Arjun,Babu,Kottayam".split(","),
            "Tins,PJ,Kottayam".split(","),
            "Vishnu,PP,Palakkad".split(","),
            "Sibin,Thomas,Kottayam".split(",")
            ]

path="output.csv"
csv_writer(data,path)   