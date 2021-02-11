# 使用turtle库绘制一个蜂窝状六边形
import turtle

turtle.setup(1080, 720, None, None)

r = 50  # 定半径
x0 = -300
y0 = 50
def draw_Agon() :
    for i in range(2,12,2) :
        turtle.penup()
        turtle.goto(x0+i*r, y0)
        turtle.pendown()
        turtle.circle(r, extent=360)  # 画圆
        turtle.penup()
        turtle.goto(x0+i*r, y0-(2*r/(3**(1/2))-r))
        turtle.pendown()  # 画六边形
        turtle.circle(2*r/(3**(1/2)), steps=6)
    # 画第二行
    y1 = y0-((3**(1/2))*r)
    for i in range(2,10,2) :
        turtle.penup()
        turtle.goto(x0+(i+1)*r, y1)
        turtle.pendown()
        turtle.circle(r, extent=360)  # 画圆
        turtle.penup()
        turtle.goto(x0+(i+1)*r, y1-(2*r/(3**(1/2))-r))
        turtle.pendown()  # 画六边形
        turtle.circle(2*r/(3**(1/2)), steps=6)
    # 画第三行，相当于只第一行坐标下移
    y2 = y1-((3**(1/2))*r)
    for i in range(4,10,2) :
        turtle.penup()
        turtle.goto(x0+i*r, y2)
        turtle.pendown()
        turtle.circle(r, extent=360)  # 画圆
        turtle.penup()
        turtle.goto(x0+i*r, y2-(2*r/(3**(1/2))-r))
        turtle.pendown()  # 画六边形
        turtle.circle(2*r/(3**(1/2)), steps=6)
    return None

draw_Agon()
