import turtle
import math

x0 = -365
y0 = 0
t = 0.15
alpha = 1.12

v0x = 25
v0y = 43.301
g = 10

x = x0
y = y0
vy = v0y


turtle.goto(-300, 0)
turtle.goto(500, 0)
turtle.goto(x0, y0)
turtle.speed(10000)

while y >= -10:
    if y < 0:
        v0x /= 1.34
        vy = v0y / alpha
        y = y0
        alpha *= 1.12
    else:
        turtle.goto(x,y)
        x += v0x * t
        y += vy * t
        vy -= g * t
    if x >= 450:
        y = -20
