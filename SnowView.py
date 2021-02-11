# SnowView.py
from turtle import *

from random import *

def drawSnow() :
    hideturtle()
    pensize(2)
    for i in range(100) :  # 画100片雪花
        r, g, b = random(), random(), random()  # 设置颜色
        pencolor(r, g, b)
        penup()  # 移动到随机位置
        setx(randint(-350, 350))  # 可以用goto(randint(-350, 350), randint(1, 270))
        sety(randint(1, 270))
        dens = randint(8, 12)  # 确定雪花瓣数
        snowsize = randint(10, 14)  # 调雪花大小
        pendown()  # 落笔
        for j in range(dens) :  # 开始画，直到转完一圈
            forward(snowsize)
            back(snowsize)
            right(360/dens)  # 顺时针转(360/dens)°，



def drawGround() :
    hideturtle()
    for i in range(400) :  # 前闭后开，画400条线
        pensize(randint(5,10))  # 全闭
        x = randint(-400, 350)
        y = randint(-280, -1)
        r, g, b = -y/280, -y/280, -y/280  # 纵向渐变色
        pencolor(r, g, b)
        penup()
        goto(x, y)  # 画下一条线
        pendown()
        forward(randint(40,100))  # 全闭



def main() :
    setup(800, 600, 200, 100)
    tracer(False)
    bgcolor('black')
    drawSnow()
    drawGround()
    done()



main()
