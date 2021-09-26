import turtle
import math
turtle.shape('turtle')
d = 30
def mn(x):
    for i in range(x):
        turtle.forward(d)
        turtle.left(360 / x)
for i in range(3, 15) :
    R = d / (2 * math.sin(math.pi/i))
    turtle.left(90 + 180/i)
    mn(i)
    turtle.right(90 + 180/i)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()
    d = 2 * (R + 10) * math.sin(math.pi/(i + 1))

