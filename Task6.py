#Answere the question 001

my_nums = [15, 81, 5, 17, 20, 21, 13]

my_nums.sort(reverse=True)
 
count=1
 
for num in my_nums:
     
    if num % 5==0:
            
        print(f"{count} => {num}")
            
        count +=1
        
    else:
        pass

print("The Loop is finished")

#------------------------------------------------------------

#Answere the question 002

my_loop = range(1,21)

for num in my_loop:

    if num < 10 and num !=6 and num !=8 and num !=12:

        print(str(num).zfill(2))

    elif num==6 or num==8 or num==12:

        continue

    else:

        print(num)

print("The Loop is finished")

#------------------------------------------------------------

#Answere the question 003

my_ranks = {
  'Math': 'A',
  "Science": 'B',
  'Drawing': 'A',
  'Sports': 'C'
}

my_points = {
    "A": 100,
    "B": 80,
    "C": 40
}

sum=0

for ranks in my_ranks:

    for points in my_points:

        if my_ranks[ranks] == points:

            sum += my_points[points]

            print(f"My Rank in {ranks} is {my_ranks[ranks]} And This Equal {my_points[points]} points")

print(f"Total Points Is: {sum}")

#------------------------------------------------------------

#Answere the question 004

students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }

}

my_points={
    "A": 100,
    "B": 80,
    "C": 40,
    "D": 20
}


sum1=0

sum2=0

sum3=0

for stud in students:
    
    print("-" * 30)
    
    print(f"Student Name => {students}")
    
    print("-" * 30)
    
    for subj in students[stud]:
     
        for points in my_points:
     
            if students[stud][subj] == points and stud == "Ahmed":
                
                sum1 += my_points[points]
                
                print(f"- {subj} => {my_points[points]} Points")
                
            elif students[stud][subj] == points and stud == "Sayed":
                
                sum2 += my_points[points]
                
                print(f"- {subj} => {my_points[points]} Points")
            
            elif students[stud][subj] == points and stud == "Mahmoud":
                
                sum3 += my_points[points]
              
                print(f"- {subj} => {my_points[points]} Points")
                
    print(f"= Total Points For {stud} Is: {sum1 if stud == 'Ahmed' else sum2 if stud == 'Sayed' else sum3}")