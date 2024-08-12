"""It's A password generator
The User Give me the length of the password and after that i generate the password
the password length must be more than 5 characters
The password consists of:  60% letters  : 30% upper cases , 30% lower cases 
                            20% digits
                            20% special characters
I Used string Module to get the components of the password
I Used random Module to make the password shuffled
"""


#Import The Modules
import string
import random
upper_cases=list(string.ascii_uppercase) # get the Upper cases characters
lower_cases=list(string.ascii_lowercase)# get the Lower cases characters
digits=list(string.digits)#get the digits
special_char=list(string.punctuation) #get the special characters
password_length=input("What Is Your Password Length? \n") #get the password length from the user
while True : # This loop to check that the length of the password is more than 5  characters and to avoid getting invalid data type from the user  
    try:
        password_length=int(password_length) #convert the password length from string to intger
        if password_length < 6 : # check the length of the password
            password_length = input("The Length Must Be More Than 5 Characters \n Plese Enter The Length Again : ")
        else:
            break   
    except ValueError:
        password_length=input("Invalid Input \n Pelese Enter Number: ")
"In The Next 4 sentence  each component of the password to be list to sure that the password will cover all cases"
random.shuffle(upper_cases)
random.shuffle(lower_cases)
random.shuffle(digits)
random.shuffle(special_char)
password=[]
part1=round(password_length*(30/100)) #Make the 60% string
part2=round(password_length*(20/100)) #Make the 40% digits and special characters
for i in range(part1):#append the upper and lower character to the password
    password.append(upper_cases[i])
    password.append(lower_cases[i])
for i in range(part2):#append the digits and the special characters to the password
    password.append(digits[i])
    password.append(special_char[i])
random.shuffle(password)
password="".join(password)        
print(f"Your Password Is : {password}") #generate the password