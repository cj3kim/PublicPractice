import turtle,threading
from math import sin, cos, radians, sqrt

window = turtle.Screen()


myT  = turtle.Turtle()


growth = lambda n: (n, (1 + (1.0/n))**n)

results = map(growth, range(1,100, 1))
for x in results: print x

for coord in results:
    myT.setpos(coord[0], coord[1])

window.exitonclick()
