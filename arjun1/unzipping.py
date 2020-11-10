from zipfile import ZipFile


file_name="arjun1.zip"

with ZipFile(file_name,'r') as zip1:
    zip1.printdir()

    print("Extracting fles here.......")
    zip1.extractall()
    print("Successfully done ....!")