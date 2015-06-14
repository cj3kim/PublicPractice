import turtle,threading
from math import sin, radians

window = turtle.Screen()


myT  = turtle.Turtle()
myT.speed(0)
sine_list = []
amplitude = 100

x = 0

while (amplitude > 0):
    fx = amplitude *  sin(radians(x))
    if x % 360  == 0: amplitude -= 10
    sine_list.append([x, fx])
    x += 1

for coord in sine_list:
    myT.setpos(coord[0]/10, coord[1])


window.exitonclick()
