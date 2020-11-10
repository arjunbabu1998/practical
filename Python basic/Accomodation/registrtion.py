import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="codergap"

)


class Registration:

    def validation(*data):
        if data[0]=="":
            return "Name is empty"
        elif data[1]=="":
            return "Email is empty"
        elif data[2]=="":
            return "No number inserted"
        elif data[3]=="":
            return "Address is empty"
        elif data[4]=="":
            return "No pincode inserted"
        elif data[5]=="":
            return "Please enter password"
        elif data[6]=="":
            return "Please confirm password"
        elif data[5]!=data[6]:
            return "password not equal"  
        else:
            return "success"       

reg_name=input("Enter your name : ")
reg_email=input("Enter your email ID : ")
reg_mobile_no=int(input("Enter your Mobile Number : "))
reg_address=input("Enter your address : ")
reg_pincode=int(input("Ente your Pin code : "))
reg_password=input("Enter your password : ")
reg_conf_password=input("Confirm Password : ")
reg_obj=Registration()
reg_obj.validation(reg_name,reg_email,reg_mobile_no,reg_address,reg_pincode,reg_password,reg_conf_password)