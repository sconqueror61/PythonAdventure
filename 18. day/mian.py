"""import colorgram

rgb_colors=[]
colors = colorgram.extract('image.jpeg',30)
for color in colors:
	r= color.rgb.r
	g= color.rgb.g
	b= color.rgb.b
	new_color=(r,g,b)
	rgb_colors.append(new_color)

print(rgb_colors)"""
import turtle as turtle_module
import random

turtle_module.colormode(255)
tim= turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list =[(245,243,238),(247,242,244),(240,245,241),(202,164,109),(238,240,245),(150,75,49),(223,201,135),(18,86,90),(81,148,129),(148,17,20),(14,70,64),(30,68,100),(107,127,153),(174,94,97),(176,192,209)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots=101

for dot_count in range(1,number_of_dots):
	tim.dot(20,random.choice(color_list))
	tim.forward(50)
	
	if dot_count %10==0:
		tim.setheading(90)
		tim.forward(50)
		tim.setheading(180)
		tim.forward(500)
		tim.setheading(0)

screen= turtle_module.Screen()
screen.exitonclick()




