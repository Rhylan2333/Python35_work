#在_____处填写一行代码
#不允许修改其他代码

import turtle
edge = 6
d = 0
k = 1
for j in range(10):
    for i in range(edge):
      turtle.fd(k)
      d += 360/edge
      turtle.seth(d)
      k += 3
turtle.done()
