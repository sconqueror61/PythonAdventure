"""student_heights=input().split()
for n in range(0,len(student_heights)):
	student_heights[n]= int(student_heights[n])
print(len(student_heights))

total_height=0
for height in student_heights:
	total_height += height
print(f"total height={total_height}")

number_of_students = 0
for student in student_heights:
	number_of_students+=1
print(f"number of students = {number_of_students}")

average_hight = round(total_height/number_of_students)
print(f"average height = {average_hight}")"""

"""student_scores=input().split()
for n in range(0,len(student_scores)):
	student_scores[n]=int(student_scores[n])
highest_score=0
for score in student_scores:
 if score > highest_score:
      highest_score=score
print(score)"""

"""target = int((input().split()))

even_sum=0
for number in range(2,target + 1,2):
	even_sum+=number
	print(even_sum)

alternative_sum=0
for number in range(1,target+1):
 if number %2 ==0:
      alternative_sum+=number
print(alternative_sum)"""

"""for numbers in range(1,101):
	if numbers %3==0:
		print("Fizz")
	elif numbers %5==0:
		print("Buzz")
	elif numbers %3==0 and numbers %5==0:
		print("FrizzBuzz")
	else:
		print(numbers)"""

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list=[]
for char in range(1, nr_letters+1):
	password_list.append(random.choice(letters))

for char in range(1,nr_symbols+1):
	password_list.append(random.choice(symbols))

for char in range(1,nr_numbers+1):
	password_list.append(random.choice(numbers)	)

"""print(password_list)	
random.shuffle(password_list)
print(password_list)
"""
password =""
for char in password_list:
	password+=char
print(f"Your password is {password_list}")

