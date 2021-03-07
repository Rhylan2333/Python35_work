# 请在______处补充一行代码
# 请不要修改其他代码
# 在IDLE运行时，请去掉代码注释部分。


import turtle
r = 10
dr = 50
head = 90
for i in range(4):
    turtle.pendown()  # 画圆都是向左转
    turtle.circle(r)
    r +=  dr
    turtle.penup()
    turtle.seth(-head)
    turtle.fd(dr)
    turtle.seth(0)
turtle.done()
