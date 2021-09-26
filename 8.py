import turtle
turtle.shape('turtle')
x = 20
for i in range(1, 10) :
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x + 10)
    turtle.left(90)
    x += 10
