import turtle


def circle(r, color):
    turtle.begin_fill()
    turtle.color(color)
    for i in range(100):
        turtle.forward(r)
        turtle.left(360/100)
    turtle.end_fill()

    
def duga(r, l):
    turtle.color('red')
    turtle.circle(r, l)
    


turtle.shape('turtle')
turtle.speed(1000000)
circle(10,'yellow')
turtle.penup()
turtle.left(65)
turtle.forward(220)
circle(1.5,'blue')
turtle.penup()
turtle.left(100)
turtle.forward(150)
turtle.pendown()
circle(1.5,'blue')
turtle.penup()
turtle.right(180)
turtle.forward(65)
turtle.right(75)
turtle.forward(25)
turtle.pendown()
turtle.width(10)
turtle.color('gray')
turtle.forward(50)
turtle.penup()
turtle.right(75)
turtle.forward(80)
turtle.right(-90)
turtle.pendown()
turtle.width(10)
duga(80,160)

