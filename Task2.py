#Answere the question 001

#Multiple Line Comment

#test...test

#------------------------------------------------------------------------

#Answere the question 002

name="Abdulrahman"   #instialize a variable with name

age="21"             #instialize a variable with age

country="Egypt"      #instialize a variable with country name

#------------------------------------------------------------------------

#Answere the question 003

print("Name: " + name)      #Print name with label
print("Age: "+ age)         #Print age with label
print("Country: "+ country) #Print country with label

#This code prints a person's name, age, and country

#------------------------------------------------------------------------

#Answere the question 004

print("Hello, My Name Is" + " " + name + " " + "And Iam" + " " + age + " " + "and I Live in" + " " + country) 

#This code prints a welcome message with the data of the person 

#------------------------------------------------------------------------

#Answere the question 005

print(type(name))       #Print the data type of the name variable

print(type(age))        #Print the data type of the age variable

print(type(country))    #Print the data type of the country variable

#This code check the data types of name, age, and country variables

#------------------------------------------------------------------------

#Answere the question 006

name ="Abdulrahman"     #instialize a variable with name

age ="21"               #instialize a variable with age

country ="Egypt"        #instialize a variable with country name

print('Hello %s How You Doing? \\""" Your age is "%s"" And Your Country is: %s'%(name,age,country))

#This code print a formatted message with name, age, and country

#------------------------------------------------------------------------

#Answere the question 007

print('Hello %s How You Doing? \ \n""" Your age is %s""  \nAnd Your country is: %s'%(name,age,country))

#This code print a formatted message with name, age, and country

#------------------------------------------------------------------------

#Answere the question 008

name="Abdulrahman"                      #instialize a variable with name

print("Second Letter Is "+(name[1]))    #print the character at index 1

print("Third Letter Is "+(name[2]))     #print the character at index 2

print("Last Letter Is "+(name[-1]))     #print the character at index -1

#This code print the different index of the string

#------------------------------------------------------------------------

#Answere the question 009

name="Abdulrahman"          #instialize a variable with name

print(name[1:4])            #print the character from index 1 to 4

print(name[::2])            #print the character from index 0 to 10 with step by 2

print(name[-1::-2])         #print the character from index -1 to 0 with step by -2

#This code is print the different index of the string

#-----------------------------------------------------------------------

#Answere the question 010

name="#@#@Abdulrahman#@#@"          #instialize a variable with name

print(name.strip("@#"))             #print the name with strip function

#This code is print the name after removing symbols using strip

#-----------------------------------------------------------------------

#Answere the question 011

num1="9"                    #instialize a variable with number

num2="15"                   #instialize a variable with number

num3="130"                  #instialize a variable with number

num4="950"                  #instialize a variable with number

num5="1500"                 #instialize a variable with number

print(num1.zfill(4))        #print the string with add 4 zeros

print(num2.zfill(4))        #print the string with add 3 zeros

print(num3.zfill(4))        #print the string with add 2 zeros

print(num4.zfill(4))        #print the string with add 1 zeros

print(num5.zfill(4))        #print the string with add 0 zeros

#This code is print the string after adding zeros using zfill

#--------------------------------------------------------------------------

#Answere the question 012

name_one="Abdulrahman"              #instialize a variable

name_two="Abdulrahman_Ashraf"       #instialize a variable

print(name_one.rjust(20,"@"))       #print the name with add @ at the start

print(name_two.rjust(20,"@"))       #print the name with add @ at the start

#This code is print the string after adding @ using rjust

#--------------------------------------------------------------------------

#Answere the question 013

name_one="ABdulrahmaN"          #instialize a variable

name_two="abdulrahmAN"          #instialize a variable

print(name_one.swapcase())      #print the name with make all uppercase lowercase and vice versa

print(name_two.swapcase())      #print the name with make all uppercase lowercase and vice versa

#This code is print the string make all uppercase lowercase and vice versa using swapcase

#---------------------------------------------------------------------------

#Answere the question 013

msg="I Love Python And Although Love Elzero Web School"     #instialize a variable

print(msg.count("Love"))                                    #print the count of word "Love"

#This code is print the count of the word with count

#---------------------------------------------------------------------------

#Answere the question 014

name="Abdulrahman"          #instialize a variable

print(name.index("d"))      #print the number of index "d"

#This code is print the index of the string with index

#---------------------------------------------------------------------------

#Answere the question 015

msg="I <3 Python And Although <3 Elzero Web School"     #instialize a variable

print(msg.replace('Love', '<3', 1))               #print the string with replace the first"<3" with "Love"

#This code is print the string with replace the first specific word with other word with replace

#---------------------------------------------------------------------------

#Answere the question 016

msg="I <3 Python And Although <3 Elzero Web School"     #instialize a variable

print(msg.replace('Love', '<3'))        #print the string with replace the all "<3" with "Love"

#This code is print the string with replace all the specific word with other word with replace

#---------------------------------------------------------------------------

#Answere the question 017

name="Abdulrahman"      #instialize a string variable

age=21                  #instialize a int variable

country="Egypt"         #instialize a string variable

print(f"My name Is {name}, And My Age Is {age}, And My Country Is {country}")

#This code is print a formatted message with name, age, and country using format

#----------------------------------------------------------------------------

#Answere the question 018

print(type(1))      #Print the data type of the number variable
print(type(1.1))    #Print the data type of the number variable
print(type(1+1j))   #Print the data type of the number variable

#This code check the data types of number variable

#----------------------------------------------------------------------------

#Answere the question 019

num=1+2j            #instialize a number variable

print(num.imag)     #Print the imaginary part of the complex number

print(num.real)     #Print the real part of the complex number

#This code check the complex number and real number

#-----------------------------------------------------------------------------

#Answere the question 020

num=10                          #instialize a number variable

print("{:.10f}".format(num))    #Print the float number after convert from int

#This code is covert the integer number to floating number with format

#-----------------------------------------------------------------------------

#Answere the question 021

num=159.650                 #instialize a number variable

num2=int(num)               #casting a number to be int

print(num2)                 #print the number

print(type(num2))           #Print the data type of the number variable

#This code check the data types of number variable

#-----------------------------------------------------------------------------

#Answere the question 022

print(100 - 115)

print(50 * 30)

print(21 % 4)

print(110 / 11)

print(97 // 20)

#This code check the arithmatical expressions

#-----------------------------------------------------------------------------