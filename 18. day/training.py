"""from turtle import Turtle,Screen"""
"""tim = Turtle()
tom=Turtle()
terry = Turtle()"""

"""timmy_the_turtle= Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)"""

"""timmy_the_turtle.forward(100)
timmy_the_turtle.left(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.left(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.left(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.left(90)

screen= Screen()
screen.exitonclick()"""

"""import turtle as t
timmy=t.Turtle()

import heroes
print(heroes.gen())"""

"""tim=Turtle()

tim.forward(18)
tim.penup()
tim.forward(18)
tim.pendown()

screen= Screen()
screen.exitonclick()"""
"""
import turtle as t
import random
tim= t.Turtle()
colors=["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen"]

def draw_shape(num_sides):
	for _ in range(num_sides):
		angle= 360 / num_sides
		tim.forward(100)
		tim.right(angle)

for shape_side_n in range(3,11):
	tim.color(random.choice(colors))
	draw_shape(shape_side_n)"""

import turtle as t
import random
tim=t.Turtle()
t.colormode(255)
def random_color():
	r=random.randint(0,255)
	g=random.randint(0,255)
	b=random.randint(0,255)
	color=(r,g,b)
	return color

tim.speed("fastest")

def draw_spirograph(size_of_graph):
	for _ in range (int(360/size_of_graph)):
		tim.color(random_color())
		tim.circle(100)
		tim.setheading(tim.heading()+size_of_graph)

draw_spirograph(5)

screen=t.Screen()
screen.exitonclick()



