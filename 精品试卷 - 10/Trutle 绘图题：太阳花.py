#在_____完善一行代码

import turtle
turtle.color('red', 'yellow')#画笔颜色与填充设置，前画笔颜色，后填充颜色
turtle.begin_fill()  # 启动填充
#绘制太阳花形状
for i in range(50):  # 画50瓣
    turtle.fd(200) #先前200
    turtle.right(170)  #右转170度
turtle.end_fill()  # 到这才填充
turtle.done()
