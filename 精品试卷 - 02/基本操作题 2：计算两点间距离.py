"""
基本操作题 2：计算两点间距离
"""

# 请在______处使用一行代码或表达式替换
#
# 注意：请不要修改其他已给出代码

ntxt = input("")
nls = ntxt.split(" ")
x1 = eval(nls[0])
y1 = eval(nls[1])
x2 = eval(nls[2])
y2 = eval(nls[3])
r = pow(pow(x2-x1, 2) + pow(y2-y1, 2),  0.5) 
print("{:.2f}".format(r))
