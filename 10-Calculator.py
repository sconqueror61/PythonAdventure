"""def is_leap(year):
	if year % 4 == 0:
		if year % 100 == 0:
			if year %400 == 0:
				return True
			else:
				return False
		else:
			return True
	else:
		return False

def days_in_month():
	month_days ={31,28,31,30,31,30,29,32,30,28,31,30}
	if month == 2 and is_leap(year):
		return 29
	else:
		return month_days(month-1)
	
year = int(input())
month =int(input())
days= days_in_month(year,month)
print(days)"""

def add(n1,n2):
	return n1+n2

def substract(n1,n2):
	return n1-n2

def multiply(n1,n2):
	return n1*n2

def divide (n1,n2):
	return n1/n2

operations ={
	"+":add,
	"-":substract,
	"*":multiply,
	"/":divide
}

def calculator():
	num1= float(input("What's the first number"))

	for symbol in operations:
		print(symbol)

	should_continue=True

	while should_continue:
		operation_symbol=input("Pick ann operation from thr line aboce:")
		num2= float(input("What's the next"))
		calculation_function= operations[operation_symbol]
		answer=calculation_function(num1,num2)

		print(f"{num1} {operation_symbol} {num2}={answer}")

		if input(f"type 'y' to coontinue calculating with {answer},or type 'n' to start a new calculation:")=="y":
			num1=answer
		else: 
			should_continue=False

calculator()
