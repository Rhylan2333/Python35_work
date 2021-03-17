#在_____处填写一行代码
#在…处填写多行代码
#允许修改其他代码

import jieba
import turtle as t

def drawCircle(x,y,radius,color,name):
    t.pencolor(color)
    t.penup()
    t.____(1)____
    t.write(name, font=('Arial', 10, 'normal'))
    t.seth(__(2)___)
    t.pendown()
    t.circle(__(3)___)
    return t.pos()

dws = {}
with open('lizhi.txt', 'r') as f:
    for l in f.readlines():
        ws = _____(4)_______
        for w in ws:
            if ___(5)____:
               dws[w] = dws.get(w,0) + 1

dls = list(dws.items())
dls.sort(key = lambda x:x[1], reverse= True)

x,y = -300,0
for i in range(10):
    print(_____(6______)
    x,y = drawCircle(x,y,dls[i][1]*4 ,'red',____(7)_____))
    x +=  _____(8)______
t.done()