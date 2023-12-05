"""numbers=[1,2.3]
new_nubers = [n+1 for n in numbers]

name ="Angela"
letters_list=[letter for letter in name]

range_list = [num*2 for num in range(1,5)]
names=["Alex", "Beth","Caroline","Dave","Elanor","Freddie"]
short_names=[n for n in names if len(n)<5]

lon_names= [name.upper() for name in names if len(name)>5]"""

"""numbers= [1,1,2,3,5,8,13,21,34,55]
square_number=[num*num for num in numbers]
print(square_number)"""

"""list_of_strings=input().split(',')
numbers=[int(x) for x in list_of_strings]
result=[num for num in numbers if num%2==0]
print(result)"""

"""names=["Alex","Beth","Caroline","Dave","Elanor","Freddie"]
import random
student_scores={student:random.randint(1,100) for student in names}

passed_students={student:score for (student,score) in student_scores.items() if score>=60}"""
"""
sentence= input()
result={word:len(word) for word in sentence.split()}"""
"""
weather_c = eval(input())

weather_f={day:temp *9/5+32 for (day,temp) in weather_c.items()}
print(weather_c.items())
print(weather_f)"""

"""student_dict= {
	"student":["Angela", "James","Lilly"],
	"score":[56,76,98]
}

for (key,value) in student_dict.items():
	print(value)

import pandas
student_data_frame=pandas.DataFrame
(student_dict)
print(student_data_frame)

for(index,row) in student_data_frame.iterrows():
	print(row.student)"""