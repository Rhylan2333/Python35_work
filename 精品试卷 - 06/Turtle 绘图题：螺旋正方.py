import turtle
d = 0
k = 1
for j in range(10):
   for i in range(4):
       turtle.fd(k)
       d += 91
       turtle.seth(d)
       k += 2
turtle.done()