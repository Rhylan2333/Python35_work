#请在、、、、补充若干行代码，完成向量积运算
ls = [111, 222, 333, 444, 555, 666, 777, 888, 999]
lt = [999, 777, 555, 333, 111, 888, 666, 444, 222]
s = 0
for x,y in zip(ls,lt):
    s += x*y
print(s)
