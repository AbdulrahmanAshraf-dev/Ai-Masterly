#Answere the question 001

print(bool(True))
print(bool("Abdulrahman"))
print(bool("9"))
print(bool(" "))
print(bool(""))
print(bool())
print(bool(False))
print(bool(None))

#------------------------------------------------------------

#Answere the question 002

html = 80

css = 60

javascript = 70

print(bool(html and css and javascript >50))

#------------------------------------------------------------

#Answere the question 003

num_one = 10

num_two = 20

num = 20

print(bool(num_one or num_two > num))

print(bool(num > num_two and num_two))

#------------------------------------------------------------

#Answere the question 004

name = input("Enter the name: ").strip().capitalize()

print(f"Hello {name}, Happy To See You Here.")

#------------------------------------------------------------

#Answere the question 005

age = int(input("Enter your age: "))

if age < 16 :
    print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")

else:
    print(f"Hello Your Age Is {age}, All Articles Is Suitable For You")


#------------------------------------------------------------

#Answere the question 006

first_name = input("Enter your the first name: ").strip().capitalize()

second_name = input("Enter your the second name: ").strip().capitalize()

print(f"Hello {first_name} {second_name:.1s}.")

#------------------------------------------------------------

#Answere the question 007

email = input("Enter your email: ").strip().lower()

print(f"Your Name Is {email.capitalize()[:email.index("@")]}")

print(f"Email Service Provider Is {email[email.index("@")+1:]}")

#------------------------------------------------------------

#Answere the question 008

num1 = int(input(" ").strip())

num2 = int(input(" ").strip())

operation = input().strip()

if(operation == "+"):
    
    print(f"{num1} + {num2} = {num1 + num2}")

elif(operation == "-"):

    print(f"{num1} - {num2} = {num1 - num2}")

elif(operation == "/"):

    print(f"{num1} / {num2} = {num1 / num2}")

elif(operation == "*"):

    print(f"{num1} * {num2} = {num1 * num2}")

elif(operation == "%"):

    print(f"{num1} % {num2} = {num1 % num2}")


#------------------------------------------------------------

#Answere the question 009

age = int(input("Enter your age: ").strip())

if(age > 16):

    print("App Is Suitable For You")
else:

    print("App Is Not Suitable For You")

#------------------------------------------------------------

#Answere the question 010

age = int(input("Enter your age: ").strip())

months = age * 12

weeks = age * months

days = age * weeks

hours = age * days

minutes = age * hours

if(age > 10 and age < 100):
    
    print(f"Your Age In Months Is {months} Month")

    print(f"Your Age In weeks Is {weeks} week")

    print(f"Your Age In days Is {days} day")

    print(f"Your Age In hours Is {hours} hour")

    print(f"Your Age In minutes Is {minutes} minute")

else:
    print("Your age out average") 

#------------------------------------------------------------

#Answere the question 011

country = input("Input Your Country: ").strip().capitalize()

countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]

price = 100

discount = 30

if(country in countries):

    print(f"Your Country Eligible For Discount And The Price After Discount Is ${price - discount}")

else:
    print(f"Your Country Not Eligible For Discount And The Price Is ${price}")