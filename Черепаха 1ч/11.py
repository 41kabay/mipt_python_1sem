import turtle as tr


def nan(n,x) :
    a = 360/n
    for i in range(0,n) :
        tr.left(a)
        tr.forward(x)
    for i in range (0,n) :
        tr.left(a)
        tr.backward(x)

tr.left(90)
for i in range(1,10,1) :
    nan(100,i)
