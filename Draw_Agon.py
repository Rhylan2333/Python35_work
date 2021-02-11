# 绘制三角形到多边形
import turtle as t

t.pensize(3)  # 三角形
t.penup()
t.goto(-200, -50)
t.pendown()
t.begin_fill()
t.color('red')
t.circle(40,steps=3)
t.end_fill()

t.penup()  # 四边形
t.goto(-100, -50)
t.pendown()
t.begin_fill()
t.color('blue')
t.circle(40, steps=4)  # 本来steps按书讲是“extent=角度”，但四边形就是把○等分成4段弧然后依次连接分割点，即steps=4
t.end_fill()

t.penup()  # 五边形
t. goto(0, -50)
t.pendown()
t.begin_fill()
t.color('green')
t.circle(40, steps=5)
t.end_fill()

t.penup()  # 六边形
t.goto(100, -50)
t.pendown()
t.begin_fill()
t.color('yellow')
t.circle(40, steps=6)
t.end_fill()

t.penup()  # 圆形
t.goto(200, -50)
t.pendown()
t.begin_fill()
t.color('purple')
t.circle(40, extent=360)
# t.down()  # 没用却不报错
t.end_fill()

t.color('black')  # 文字表示颜色
t.penup()
t.goto(-100, 100)
t.pendown()
t.write("Cool Colorful Shapes", font=("Times", 18, "bold"))
t.hideturtle()
t.done()  # 用来停止画笔绘制，但绘图窗口不关闭。
