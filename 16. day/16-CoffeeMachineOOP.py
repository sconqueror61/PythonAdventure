"""from turtle import Turtle , Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("green")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
"""
"""from prettytable import PrettyTable
tabele = PrettyTable()
tabele.add_column("Pokemon name",["Pikachu","Squirtle","Charmander"])
tabele.add_column("Type",["Electric","Water","Fire"])
tabele.align="l"
print(tabele)"""
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu=Menu()
money_machine = MoneyMachine()
coffee_maker= CoffeeMaker()
is_on=True
coffee_maker.report()
money_machine.report()

while is_on:
	options=menu.get_items()
	choice=input(f"What would you like({options})")
	if choice =="off":
		is_on=False
	elif choice== "report":
		coffee_maker.report()
		money_machine.report()
	else:
		drink=menu.find_drink(choice)
		if coffee_maker.is_resource_sufficient(drink):
			if money_machine.make_payment(drink.cost):
				coffee_maker.make_coffee(drink)
