#Answere the question 001

friends = ["Omar" , "Hisham" , "Yousif" , "Mahmoud" , "Fahd"]      # instialize a list called friends

print(friends[0])    # Print the first element of the list

print(friends[-5])   # Print the first element of the list using negative index

print(friends[-1])   # Print the fifth element of the list using negative index

print(friends[4])    # Print the last element of the list

#This code print the elements with different index

#------------------------------------------------------------

#Answere the question 002

friends = ["Omar" , "Hisham" , "Yousif" , "Mahmoud" , "Fahd"]   # instialize a list called friends

print(friends[0::2])    # Print every second element starting from the first element

print(friends[1:4:2])   # Print elements starting from the second element up to the fourth element

#This code print the elements with different index

#------------------------------------------------------------

#Answere the question 003

friends = ["Omar" , "Hisham" , "Yousif" , "Mahmoud" , "Fahd"]   # instialize a list called friends

print(friends[1:4]) # Print element starting from the second element up to the third element

print(friends[3:5]) # Print element starting from the third element up to the fourth element

#This code print the elements with different index

#-----------------------------------------------------------

#Answere the question 004

friends = ["Omar" , "Hisham" , "Yousif" , "Mahmoud" , "Fahd"]   # instialize a list called friends

friends[3] = "Elzero"   # replace the fourth element 

friends[4] = "Elzero"   # replace the fifth element 

print(friends)  # print the list called friends

#------------------------------------------------------------

#Answere the question 005

friends = ["omar" , "Hisham" , "Yousif"]    # instialize a list called friends

friends.insert(0 , "Nasser")    # insert the first element with the new element

print(friends)  # print the list

friends.append("Nasser")    # add new element to list 

print(friends)  # print the list called friends

#-----------------------------------------------------------

#Answere the question 006

friends = ["Omar" , "Hisham" , "Yousif" , "Mahmoud" , "Fahd"]   # instialize a list called friends

friends = friends[2:]   # delete first two elements in the list

print(friends)  # print the list called friends

friends.pop(2)  # delete the second element in the list

print(friends)  # print the list called friends

#----------------------------------------------------------

#Answere the question 007

friends = ["Omar" , "Hisham"]   # instialize a list called friends

employees = ["Samah" , "Eman"]  # instialize a list called employees

school = ["Ramy" , "Shady"] # instialize a list called school

friends.extend(employees)   # add list of employees to the list of friends

friends.extend(school)  # add list of school to the list of friends

print(friends)  # print the list called friends

#---------------------------------------------------------

#Answere the question 008

friends = ['Omar', 'Hisham', 'Samah', 'Eman', 'Ramy', 'Shady']  # instialize a list called friends

friends.sort()  # sort the list alphabetical

print(friends)  # print the list called friends

friends.reverse()   # reverse the elements in the list 

print(friends)  # print the list called friends

#---------------------------------------------------------

#Answere the question 009

friends = ['Omar', 'Hisham', 'Samah', 'Eman', 'Ramy', 'Shady']  # instialize a list called friends

print(len(friends)) # print the numbers of the elements of the list called friends

#---------------------------------------------------------

#Answere the question 010

technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]  # instialize a list called technlolgies

print(technologies[-1][0])  # Print the first element in the element who knows with inner list  

print(technologies[-1][-1]) # print the last element in element who knows with inner list

#---------------------------------------------------------

#Answere the question 011

name = "Abdulrahman",   # instialize a tuple called name

print(name) # print the tuple called name

print(type(name))   # print the type of the tuple

#---------------------------------------------------------

#Answere the question 012

friends = ("Osama" , "Omar" , "Hisham") # instialize a tuple called friends

friendsList = list(friends) # convert the tuple to a list

friendsList [0] = "Elzero"  # replace the first element of the list with "Elzero"

friends = tuple(friendsList)    # convert the list to a tuple

print(friends)  # print the tuple called friends

print(type(friends))    # print the type of the tuple

print(f"{len(friends)} Elments")    # print the number of elements in the tuple

#---------------------------------------------------------

#Answere the question 013

nums = (1, 2, 3)    # instialize a tuple called nums

letters = ("A", "B", "C")   # instialize a tuple called letters

nums_and_letters_one = nums + letters

print(nums_and_letters_one)

print(f"{len(nums_and_letters_one)} Elements")

#--------------------------------------------------------

#Answere the question 014

my_tuple = (1, 2, 3, 4)     # instialize a tuple called my_tuple

A , B , _ , C = my_tuple    # unpack values from the tuple into variables

print(A)    # print the value A

print(B)    # print the value B

print(C)    # print the value C 

#-------------------------------------------------------

#Answere the question 015

my_list = [1, 2, 3, 3, 4, 5, 1] # instialize a list called my_list

unique_list = list(set(my_list))    # find the elements in the list and convert them back to a list

print(unique_list)  # print the list called unique_list

print(type(unique_list))    # print the type of the list called unique_list

print(unique_list[0:4])     # print the first four elements in the list called unique_list

#-------------------------------------------------------

#Answere the question 016

nums = {1, 2, 3}    # instialize a list called nums

letters = {"A", "B", "C"}   # instialize a list called letters

print(nums.union(letters))  # print the union elements between the two lists nums and letters

print(nums | letters)   # another way to print the union of elements using the "|" operator

nums.update(letters)    # update the set nums with the elements from set letters

print(nums) # print the update set nums

#-------------------------------------------------------

#Answere the question 017

my_set = {1, 2, 3}  # instialize a list called my_set

letters = {"A", "B", "C"}   # instialize a list called letters

print(my_set)   # print the set called my_set

my_set.clear()  # clear the set called my_set

print(my_set)   # print the set called my_set after cleared it

letters.discard("C")    # discard a element in the set 

print(letters)  # print the set called letters after discared a element from it

#------------------------------------------------------

#Answere the question 018

set_one = {1, 2, 3} # instialize a list called set_one

set_two = {1, 2, 3, 4, 5, 6}    # instialize a list called set_two

print(set_one.issubset(set_two))    # print the subset of the set_one from set_two

#------------------------------------------------------

#Answere the question 019

skills = {
    "HTML" : "Is 90%",
    "CSS" : "Is 80%",
    "Python" : "Is 30%"
}    # define a dictionary called skills with keys representing skills and values representing progress

skills.update({"AI" : "Is 20%"})    # update the skills dictionary with a new key-value

print(f"HTML Progress Is {skills['HTML']}") # print the progress for each skill
print(f"CSS Progress Is {skills['CSS']}")   # print the progress for each skill
print(f"Python Progress Is {skills['Python']}") # print the progress for each skill
print(f"AI Progress Is {skills['AI']}") # print the progress for each skill

#------------------------------------------------------