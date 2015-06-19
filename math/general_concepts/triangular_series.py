

import turtle,threading
from math import sin, cos, radians, sqrt

#The triangular series. Great for solving handshake problems and finding the optimal amount of
#steps between 0 -> N.

window = turtle.Screen()
myT  = turtle.Turtle()

_const = 100
_range = range(0,500)
results = zip(_range, map(lambda x: x/_const, map(lambda n: (n**2 + n)/2, _range)))


for coord in results:
    myT.setpos(coord[0],coord[1])

window.exitonclick()
