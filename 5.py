import turtle
turtle.shape('turtle')
def nn(n,x) :
    a = 360 / n
    for i in range(0, n) :
        turtle.forward(x)
        turtle.left(a)
for i in range(1, 10) :
    nn(4, i * 20)
    turtle.penup()
    turtle.backward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.left (90)
    turtle.pendown()
