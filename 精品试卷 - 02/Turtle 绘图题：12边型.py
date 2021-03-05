# 请在______完善代码,删除横线。
# 最后请用Print 输出你的结果，供系统评分。
import turtle
turtle.pensize(2)
d=0
for i in range(1, 13):
##    turtle.pd()  # 初始状态下就是pendown()
    turtle.forward(40)
    d += 30
    turtle.seth(d)
