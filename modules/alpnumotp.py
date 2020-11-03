import math, random 
 
def OTPgenerator() : 

	string= '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	OTP = "" 
	length = len(string)
	for i in range(8) : 
		OTP += string[math.floor(random.random() * length)] 

	return OTP 


# Main Function 

print("Your 8 digit alphanumeric OTP is: ", OTPgenerator())