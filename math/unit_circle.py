import turtle,threading
from math import sin, cos, radians, sqrt

window = turtle.Screen()


myT  = turtle.Turtle()

amp = 150 
unit_circle_coords = map(lambda t: (amp * sin(t), amp * cos(t)), range(0,100,1))

for coord in unit_circle_coords: myT.setpos(coord[0], coord[1])

window.exitonclick()
