import turtle
def w(n, x) :
    a = 360 / n
    for i in range(0, n) :
        turtle.left(a)
        turtle.forward(x)
for i in range(54, 360, 12) :
    w(100, 5)
    turtle.right(i)
        
