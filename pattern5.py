
import turtle

# defining colors
colors = ['red', 'yellow', 'green',  'blue']

# setup turtle pen
t= turtle.Pen()

# changes the speed of the turtle
t.speed(11)

# changes the background color
turtle.bgcolor("black")

# make spiral_web
for x in range(250):
	t.pencolor(colors[x%4]) # setting color
	t.width(x/100 + 1) # setting width
	t.forward(x) # moving forward
	t.left(59) # moving left

turtle.done()
t.speed(10)

turtle.bgcolor("black") # changes the background color

# make spiral_web
for x in range(300):
	t.pencolor(colors[x%4]) # setting color
	t.width(x/100 + 1) # setting width
	t.forward(x) # moving forward
	t.left(59) # moving left

turtle.done()
