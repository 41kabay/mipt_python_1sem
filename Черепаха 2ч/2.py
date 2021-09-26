import turtle
from random import *

turtle.shape('turtle')
turtle.color('red')
i = 1000
while i > 0:
    turtle.forward(randint(0, 50))
    turtle.left(randint(0, 90))
