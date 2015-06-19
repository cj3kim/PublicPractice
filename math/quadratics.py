import turtle,threading
from math import sin, cos, radians, sqrt

window = turtle.Screen()
myT  = turtle.Turtle()

a= 0.002
c = 200
quad = lambda x: (x, (-a * x**2 + c))


r = 300

results = map(quad, range(-r,r,1))

for coord in results:
    myT.setpos(coord[0], coord[1]) 

window.exitonclick()
