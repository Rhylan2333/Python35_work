# -*- coding:utf-8 -*-
'''
This is a python123.io file.
'''
s = input() # 请输入一个由1和0组成的二进制数字串
d = 0
while s:
    d = d*2 + (int(s[0]) - 0)
    s = s[1:]
print("转换成八进制数是：{:o}".format(d))
