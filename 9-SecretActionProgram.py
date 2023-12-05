"""programing_dictionary= {
"Bug":"xdfcgvhbjnmkölç",
"Function":"ghjkmlölç"
}

programing_dictionary["Loop"]="cvbnjkmlöş"
print(programing_dictionary)

empty_dictionary ={}

programing_dictionary=empty_dictionary

programing_dictionary["Bug"]="A moth on your computer"
print(programing_dictionary)

for key in programing_dictionary:
	print(key)
	print(programing_dictionary[key])"""
"""
student_scores={
	"Ömer":61,
	"Seyfullah":61,
	"Fatih":61
}

student_grades={}

for student in student_scores:
	score=student_scores[student]
	if score>90:
		student_grades[student]="Outstanding"
	elif score >80:
		student_grades[student]="Exceedes expectations"
	elif score>70:
		student_grades[student]="Acceptable"
	else:
		student_grades[student]="Fail"

print(student_grades)"""

"""
capitals={"France": "Paris",
		  "Germany":"Berlin"}

travel_log={
	"France":{"cities_visited": ["Paris","Lille","Dijon"],"totalvisits":12},
	"Germany":{"cities_visited": ["Berlin","Hamburg","Stutgrat"],"total_visits":5}
}"""
"""country=input()
visits=int(input())
list_of_cities = eval(input())
travel_log=[
	{"country":"France",
  	"cities_visited": ["Paris","Lille","Dijon"],
  	"totalvisits":12},
	{"country":"Germany",
  	"cities_visited": ["Berlin","Hamburg","Stutgrat"],
	"total_visits":5}
]

def add_new_country(name,times_visited,cities_visited):
	new_country={}
	new_country["country"]=name
	new_country["visits"]=times_visited
	new_country["cities"]=cities_visited

	travel_log.append(new_country)

add_new_country(country,visits,list_of_cities)

print(f"I have been to {travel_log[2]['country']}{travel_log[2]['visits']} times")"""
from turtle import clear


bids={}
bidding_finished=False

def find_highest_bidder(bidding_record):
	highest_bid=0
	winner=""

	for bidder in bidding_record:
		bid_amount=bidding_record[bidder]
		if bid_amount>highest_bid:
			highest_bid=bid_amount
			winner=bidder
	print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
	name=input("What is your name?")
	price=int(input("What is your bid? $"))
	bids[name]=price
	should_continue=input("Are they any other bidder? yes or no")
	if should_continue =="no":
		bidding_finished=True
		find_highest_bidder(bids)
	elif should_continue=="yes":
		clear()

