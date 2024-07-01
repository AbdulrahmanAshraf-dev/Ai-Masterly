#Answere the question 001

name=input("Enter your name: ").strip().capitalize()

print(f"Hello {name}, Happy To See You Here.")

#------------------------------------------------------------

#Answere the question 002

age=int(input("Enter Your age: "))

if age > 16:
    print(f"Hello Your Age Is {age}, All Articles Is Suitable For You")
else:
    print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")

#------------------------------------------------------------

#Answere the question 003

first_name=input("Enter the first name: ").strip().capitalize()

second_name=input("Enter the second name: ").strip().capitalize()

print(f"Hello, {first_name} {second_name[0]}.")

#------------------------------------------------------------

#Answere the question 004

emails=input("Emter your email: ").strip().lower()

print(f"Your name is {emails.capitalize()[:emails.index('@')]}")

print(f"Email Service Provider Is {emails[emails.index('@')+1:emails.index('.')]}")

print(f"Top Level Domain Is {emails[emails.index('.')+1:]}")

