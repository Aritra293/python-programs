import turtle
import colorsys

t= turtle.Turtle()
s= turtle.Screen()
s.bgcolor('black')
t.speed(0)
n = 80
h = 0
for i in range(280):
    c = colorsys.hsv_to_rgb(h,1,0.8)
    h+=1
    t.color(c)
    t.left(104)
    t.forward(i)
    for j in range(3):
        t.left(5)
        t.forward(i)
