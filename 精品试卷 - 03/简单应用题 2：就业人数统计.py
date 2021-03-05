# -*- coding:utf-8 -*-
'''
This is a python123.io file.
'''
#请在...上完善代码
names=input()
ls_names = names.split()
d = {}
for name in ls_names :
    d[name] = d.get(name, 0) + 1
ls = list(d.items())
ls.sort(key=lambda x:x[1], reverse=True) # 按照数量排序
for k in range(len(ls)):
    print("{}:{}".format(ls[k][0], ls[k][1]))
