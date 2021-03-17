#在_____处填写一行代码
#在…处填写多行代码
#允许修改其他代码

import jieba
import turtle as t

def drawCircle(x,y,radius,color,name):
    t.pencolor(color)
    t.penup()
    t.goto(x,y)
    t.write(name, font=('Arial', 10, 'normal'))
    t.seth(-90)
    t.pendown()
    t.circle(radius)
    return t.pos()

dws = {}
with open('lizhi.txt', 'r', encoding='utf-8') as f:
    for l in f.readlines():
        ws = jieba.lcut(l.strip('\n'))
        for w in ws:
            if len(w) >= 2:  # 不合题设
               dws[w] = dws.get(w,0) + 1

dls = list(dws.items())
dls.sort(key = lambda x:x[1], reverse= True)

x,y = -300,0
for i in range(10):
    print(dls[i][0],dls[i][1])
    x,y = drawCircle(x,y,dls[i][1]*4 ,'red',dls[i][0]+str(dls[i][1]))
    x +=  dls[i][1] * 8
t.done()
