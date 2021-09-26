import turtle 

def duga(r,l):
    turtle.circle(r, l)


turtle.shape('turtle')
turtle.color('green')
turtle.speed(10)
turtle.penup()
turtle.goto(-250,0)
turtle.pendown()
turtle.right(90)
for i in range(1,10):
    duga(50, -180)
    duga(15,-180)
