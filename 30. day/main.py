
"""try:
	file = open("a_file.txt")
except FileNotFoundError:
	file= open("a_file.txt","w")
	file.write("Something")
except KeyError as error_message:
	print(f"The key {error_message} does not exist")
else:
	content=file.read()
	print(content)
finally:
	raise KeyError"""
"""height=float(input("Height: "))
weight=float(input("Weight: "))
if height >3 :
	raise ValueError("Human height should not be over 3 meters")
bmi = weight / height** 2
print(bmi)"""

"""fruits = eval(input())

def make_pie(index):
	try:
		fruit=fruits[index]
	except IndexError:
		print("Fruit pie")

make_pie(4)"""

facebook_posts= eval(input())

total_likes=0

for post in facebook_posts:
	try:
		total_likes=total_likes+post["Likes"]
	except KeyError:
		pass

print(total_likes)

